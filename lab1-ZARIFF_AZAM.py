import streamlit as st
import pandas as pd
from Bio import Entrez, SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

Entrez.email = "zariff@graduate.utm.my"   


def retrieve_data(id):
    # Retrieve a protein record for the given ID.
    handle = Entrez.efetch(db="protein", id=id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record


def get_basic_analysis(sequence):
    # Return length, amino acid composition, molecular weight, and pI
    analysis = ProteinAnalysis(str(sequence))
    length = len(sequence)
    composition = analysis.count_amino_acids()    
    mol_weight = analysis.molecular_weight()
    pI = analysis.isoelectric_point()
    return length, composition, mol_weight, pI


st.title('Lab 1 - ZARIFF AZAM')

protein_id = st.text_input('Enter Uniprot ID')
retrieve = st.button('Retrieve')
with st.expander("Example IDs"):
                    st.write("***Q6ZWK4*** - RHEX_HUMAN")
                    st.write("***Q92692*** - NECT2_HUMAN")
                    st.write("***U6BYK3*** - MIMOS_MIMPU")

if retrieve:
    if protein_id != "":
        try:
            record = retrieve_data(protein_id)
            length, composition, mw, pI = get_basic_analysis(record.seq)

            st.success(f"Retrieved: {record.id}")

            tab1, tab2 = st.tabs(["Basic Info", "Analysis"])

            with tab1:
                st.write("**Name:**", record.name)
                st.write("**Description:**", record.description)
                st.write("**Organism:**", record.annotations.get("organism", "N/A"))
                with st.expander("Show sequence"):
                    st.code(str(record.seq))

            with tab2:
                # leangth, mol. weight & Isoelectric point
                c1, c2, c3 = st.columns(3)
                c1.metric("Length (aa)", length)
                c2.metric("Mol. weight (Da)", f"{mw:,.2f}")
                c3.metric("Isoelectric point", f"{pI:.2f}")

                # bar chart and table (composition)
                st.subheader("Amino acid composition")
                df = pd.DataFrame(composition.items(), columns=["Amino acid", "Count"])
                st.bar_chart(df.set_index("Amino acid"))
                st.dataframe(df)

        except Exception as e:
            st.error(f"Could not retrieve or analyse that ID: {e}")
    else:
        st.warning('Please enter Uniprot ID')
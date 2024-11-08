import numpy as np
import streamlit as st
import Helpers.AlgorithmHelpers.read_dict as rd


class TwoPhase:
    def __init__(self, data: dict, threshold=30):
        self.data = data
        self.names, self.utilities = rd.read(self.data)
        self.threshold = threshold
        st.write(self.names[:5])
        st.write(self.utilities[:5])

    def run(self):
        pass

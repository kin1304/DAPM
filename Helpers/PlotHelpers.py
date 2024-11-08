import matplotlib.pyplot as plt
import mplcursors
import streamlit as st


# Bước 3: Vẽ biểu đồ scatter
def plot_algo(data: list):
    combo = []
    x = [sup[1] for sup in data]
    y = [sup[2] for sup in data]
    item = [sup[0] for sup in data]
    fig, ax = plt.subplots()
    ax.scatter(x, y, label="Utilities vs Frequency", marker="x", color="green")
    ax.set_xlabel("Tần số xuất hiện trong giao dịch")
    ax.set_ylabel("Độ hữu ích của các tập")
    for i in range(len(data)):
        combo.append(str(item[i]))
        ax.text(x[i], y[i], "item " + str(i), fontsize=9, ha='right', color='blue')
        #ax.annotate(f'{str(item[i])}', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    # Thêm chú thích tương tác khi rê chuột và tùy chỉnh
    cursor = mplcursors.cursor(ax, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'{combo[sel.index]}'))

    ax.set_title(f'Biểu đồ Scatter của frequence so với utilities')
    st.pyplot(fig)

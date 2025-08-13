import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import mpltern
import numpy as np

def read_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            name, a, b, c, img = line.split()
            data.append((name, float(a), float(b), float(c), img))
    return data

def plot_ternary_with_icons(data, zoom=0.1):
    fig = plt.figure()
    tax = fig.add_subplot(projection='ternary')
    for name, a, b, c, img_path in data:
        x, y, _ = a, b, c  # 三分量输入
        # 注：mpltern.scatter 可用辅助坐标转换
        tax.scatter([(a, b, c)], marker='.', color='none')  
        im = OffsetImage(plt.imread(img_path), zoom=zoom)
        ab = AnnotationBbox(im, (a, b, c), xycoords='data', frameon=False)
        tax.add_artist(ab)
        tax.text(a, b, name, fontsize=8, ha='center', va='center')
    tax.set_tlabel('维度1')
    tax.set_llabel('维度2')
    tax.set_rlabel('维度3')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    data = read_data('people_data.txt')
    plot_ternary_with_icons(data, zoom=0.08)

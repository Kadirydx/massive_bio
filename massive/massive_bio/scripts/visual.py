import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def ploter(csv_input, image_output):
    df = pd.read_csv(csv_input)
    plt.figure(figsize=(18, 6))
    
    # C İçeriği 
    plt.subplot(1, 3, 1)
    sns.histplot(df['GC_Content'], kde=True, color='blue')
    plt.title(f"GC Distribution\nMean: {df['GC_Content'].mean():.2f}%")
    plt.xlabel("GC %")
    
    # Okuma Uzunlukları logaritmik
    plt.subplot(1, 3, 2)
    sns.histplot(df['Read_Length'], kde=True, color='green')
    
    plt.xscale('log') 
    
    plt.title(f"Read Length Distribution (Log Scale)\nMedian: {df['Read_Length'].median():.0f} bp")
    plt.xlabel("Length (bp) - Log Scale")
    
    #kalite 
    plt.subplot(1, 3, 3)
    sns.histplot(df['Mean_Quality'], kde=True, color='red')
    plt.title(f"Quality Distribution\nMean: {df['Mean_Quality'].mean():.2f}")
    plt.xlabel("Phred Quality Score")

    plt.tight_layout()
    plt.savefig(image_output)
    print(f"Logaritmik grafikler hazırlandı: {image_output}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python scripts/visual.py <girdi_csv> <cikti_png>")
    else:
        ploter(sys.argv[1], sys.argv[2])
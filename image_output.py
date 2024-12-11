
for i in range(len()):#一層ずつ描画
    data = clear_data_list[i]
    
    fig, axes = plt.subplots(1, 12, figsize=(12*3, 3))
    for j in range(len(data)):
        axes[j].imshow(data[j])
        axes[j].axis("off")
        axes[j].set_title(f"{j+1}層目")
        
    fig.suptitle(f"number{i}", x=0.5, y=0.98, ha='left', fontsize=20, color="r")
    plt.tight_layout()
    plt.show()

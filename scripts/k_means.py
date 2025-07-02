'''
Author: Paula Tovar
Title: K-Means Clustering
Description: Two k-means models, one having 2 clusters and the other with 4. Baseline and Open Access 1 have their
             own models.
Date Created: 06/26/25
Date Last Modified: 07/02/25
'''

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
import matplotlib.pyplot as plt
import numpy as np

# functions
def k_means(data, k):
    k_means = KMeans(n_clusters = k, random_state = 0)
    labels = k_means.fit_predict(data)
    return labels, k_means

def rand_index(results_df):
    labels_true = results_df["truth_labels"]
    labels_predicted = results_df["cluster"]
    return adjusted_rand_score(labels_true, labels_predicted)

def inertia(data, start, end):
    inertia_vals = []
    for i in range(start, end + 1):
        label, k_means_obj = k_means(data, i)
        inertia_k = k_means_obj.inertia_
        inertia_vals.append(inertia_k)
    return inertia_vals

def plot(result_df, num_clusters, title):
    categories = list(result_df["drinking_category"].unique())
    categories.sort()

    # create counts dict
    dict = {}
    for i in categories:
        cat_df = result_df[result_df["drinking_category"] == i]
        count0 = (cat_df["cluster"] == 0).sum()
        count1 = (cat_df["cluster"] == 1).sum()
        dict[i] = [count0, count1]

        if num_clusters == 4:
            count2 = (cat_df["cluster"] == 2).sum()
            count3 = (cat_df["cluster"] == 3).sum()
            dict[i].append(count2)
            dict[i].append(count3)

    group_space = 0.35
    x = np.arange(num_clusters) * (1 + group_space)
    width = 0.25
    mult = 0

    fig, ax = plt.subplots()

    for category, count in dict.items():
        offset = width * mult
        rects = ax.bar(x + offset, count, width, label = category)
        ax.bar_label(rects, padding = 3)
        mult += 1

    ax.set_ylabel("Monkeys")
    ax.set_title(title)
    ax.set_xticks(x + 0.37, range(num_clusters))
    ax.legend(loc = "upper left", ncols = 4)
    if num_clusters == 2:
        ax.set_ylim(0, 45)
    else:
        ax.set_ylim(0, 25)
    plt.show()

def truth_labels(result_df, num_clusters):
    result_df["truth_labels"] = 0

    if num_clusters == 2:
        result_df.loc[result_df["drinking_category"] == "HD", "truth_label"] = 1
        result_df.loc[result_df["drinking_category"] == "VHD", "truth_label"] = 1

    else:
        result_df.loc[result_df["drinking_category"] == "VHD", "truth_label"] = 1
        result_df.loc[result_df["drinking_category"] == "LD", "truth_label"] = 2
        result_df.loc[result_df["drinking_category"] == "HD", "truth_label"] = 3

    return result_df

def model(data_df, time_df, num_clusters):
  labels, model = k_means(data_df, num_clusters)
  centers = model.cluster_centers_
  result_data = {"MATRR ID": time_df["MATRR ID"],
                 "drinking_category": time_df["drinking_category"],
                 "cluster": labels}
  results_df = pd.DataFrame(result_data)
  results_df = truth_labels(results_df, num_clusters)
  return results_df

if __name__ == "__main__":
  # read in data
  data_path = "../dat/standardized.xlsx"
  data_df = pd.read_excel(data_path)
  data_df = data_df.set_index('MATRR ID', drop = False)

  # dataframes based on timepoint
  columns_to_drop = [0, 1, 2, 3, 4, 5, 6, 7]
  baseline_df = data_df[data_df["Timepoint"] == "baseline"]
  numeric_baseline = baseline_df.drop(baseline_df.columns[columns_to_drop], axis = 1)

  open_df = data_df[data_df["Timepoint"] == "open access 1"]
  numeric_open = open_df.drop(open_df.columns[columns_to_drop], axis = 1)

  # baseline - K = 2
  baseline2_results = model(numeric_baseline, baseline_df, 2)
  plot(baseline2_results, 2, "Baseline Clustering with 2 Clusters")
  print(rand_index(baseline2_results))

  # open access 1 - K = 2
  open2_results = model(numeric_open, open_df, 2)
  plot(open2_results, 2, "Open Access 1 Clustering with 2 Clusters")
  print(rand_index(open2_results))

  # baseline - K = 4
  baseline4_results = model(numeric_baseline, baseline_df, 4)
  plot(baseline4_results, 4, "Baseline Clustering with 4 Clusters")
  print(rand_index(baseline4_results))

  # open access 1 - K = 4
  open4_results = model(numeric_open, open_df, 4)
  plot(open4_results, 4, "Open Access 1 Clustering with 4 Clusters")
  print(rand_index(open4_results))

  # optimal number of clusters
  inertia_baseline = inertia(numeric_baseline, 1, 10)
  inertia_open = inertia(numeric_open, 1, 10)

  plt.plot(range(1, 10 + 1), inertia_baseline,
           marker = "o",
           linestyle = "--",
           color = "blue",
           label = "baseline")
  plt.plot(range(1, 10 + 1), inertia_open,
           marker = "o",
           linestyle = "--",
           color = "red",
           label = "open access")
  plt.xlabel("K")
  plt.ylabel("Inertia")
  plt.title("Inertia over different number of clusters")
  plt.legend(loc = "lower left")
  plt.show()

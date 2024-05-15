<h1 align="center">🟣 Summary 🟣
</h1>

## Aim of the experiments

Three types of experiments were conducted:

1. The first one tests the storage capacity of our Hopfield network and tests if the theoretical capacities for each learning rule correspond to the empirically estimated capacities that can be seen in the summary capacity plots. A table indicates the results from this first experiment.
2. Tests to check the robustness of the Hopfield network to perturbations for different sizes of patterns for a network of two patterns were made. The number of perturbations for each tested pattern size were increment by 5% of the pattern size. These results are seen in the robustness plots. A table presents the results from this second experiment.
3. We finally tried to recall an image content from a corrupted image *i.e. here we kept the upper left corner of an image*. The retrieval of the image can been visualised in a video link at the end of this file as well as clips from the video.

*10 network size ranging logarithmically from 10 to 2500 were used to test the storage capacity and the robustness of the Hopfield network.*

<h2 align="center"> 1. Capacity tests
</h2>


<h2 align="center"> Capacity Plots for different Network sizes
</h2>

### Hebbian plots

![hebbian_capacity_of_size_10](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_10.png)

![hebbian_capacity_of_size_18](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_18.png)

![hebbian_capacity_of_size_34](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_34.png)

![hebbian_capacity_of_size_63](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_63.png)

![hebbian_capacity_of_size_116](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_116.png)

![hebbian_capacity_of_size_215](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_215.png)

![hebbian_capacity_of_size_397](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_397.png)

![hebbian_capacity_of_size_733](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_733.png)

![hebbian_capacity_of_size_1354](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_1354.png)

![hebbian_capacity_of_size_2500](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_of_size_2500.png)


### Storkey plots

![storkey_capacity_of_size_10](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_10.png)

![storkey_capacity_of_size_18](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_18.png)

![storkey_capacity_of_size_34](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_34.png)

![storkey_capacity_of_size_63](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_63.png)

![storkey_capacity_of_size_116](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_116.png)

![storkey_capacity_of_size_215](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_215.png)

![storkey_capacity_of_size_397](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_397.png)

![storkey_capacity_of_size_733](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_733.png)

![storkey_capacity_of_size_1354](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_1354.png)

![storkey_capacity_of_size_2500](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_of_size_2500.png)


<h2 align="center"> Summary Capacity Plots
</h2>

### Hebbian plot

![hebbian_summary](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/hebbian_summary_graph.png)

The empirical capacity plot for the hebbian rule obtained is very acurate with the theoretical storage capacity.


### Storkey plot

![storkey_summary](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Capacity_Graphs/storkey_summary_graph.png)

The empirical capacity plot for the storkey rule is a little bit off for the pattern size at 2500. A greatter precision could be obtained by increasing the number of iterations.


<h2 align="center"> Capacity table
</h2>

|     |   network_size | weight_rule   |   num perturb |   match_frac |   num_patterns |
|----:|---------------:|:--------------|--------------:|-------------:|---------------:|
|   0 |             10 | hebbian       |             2 |          0.7 |              2 |
|   1 |             10 | hebbian       |             2 |          1   |              1 |
|   2 |             10 | hebbian       |             2 |          0.8 |              2 |
|   3 |             10 | hebbian       |             2 |          1   |              1 |
|   4 |             10 | hebbian       |             2 |          1   |              1 |
|   5 |             10 | hebbian       |             2 |          0.8 |              2 |
|   6 |             10 | hebbian       |             2 |          0.4 |              3 |
|   7 |             10 | hebbian       |             2 |          1   |              1 |
|   8 |             10 | hebbian       |             2 |          0.9 |              2 |
|   9 |             10 | hebbian       |             2 |          1   |              1 |
|  10 |             18 | hebbian       |             3 |          0.2 |              6 |
|  11 |             18 | hebbian       |             3 |          1   |              2 |
|  12 |             18 | hebbian       |             3 |          0.9 |              3 |
|  13 |             18 | hebbian       |             3 |          0.7 |              3 |
|  14 |             18 | hebbian       |             3 |          0.8 |              4 |
|  15 |             18 | hebbian       |             3 |          0.9 |              3 |
|  16 |             18 | hebbian       |             3 |          0.5 |              5 |
|  17 |             18 | hebbian       |             3 |          0.4 |              6 |
|  18 |             18 | hebbian       |             3 |          1   |              2 |
|  19 |             18 | hebbian       |             3 |          1   |              1 |
|  20 |             34 | hebbian       |             6 |          0.3 |              8 |
|  21 |             34 | hebbian       |             6 |          0.5 |              8 |
|  22 |             34 | hebbian       |             6 |          0.8 |              4 |
|  23 |             34 | hebbian       |             6 |          0.5 |              6 |
|  24 |             34 | hebbian       |             6 |          1   |              3 |
|  25 |             34 | hebbian       |             6 |          0.3 |              8 |
|  26 |             34 | hebbian       |             6 |          0.8 |              4 |
|  27 |             34 | hebbian       |             6 |          0.6 |              6 |
|  28 |             34 | hebbian       |             6 |          0.6 |              5 |
|  29 |             34 | hebbian       |             6 |          1   |              3 |
|  30 |             63 | hebbian       |            12 |          0.5 |             11 |
|  31 |             63 | hebbian       |            12 |          1   |              3 |
|  32 |             63 | hebbian       |            12 |          0.9 |              6 |
|  33 |             63 | hebbian       |            12 |          0.1 |             13 |
|  34 |             63 | hebbian       |            12 |          0.2 |             13 |
|  35 |             63 | hebbian       |            12 |          1   |              6 |
|  36 |             63 | hebbian       |            12 |          0   |             15 |
|  37 |             63 | hebbian       |            12 |          1   |              3 |
|  38 |             63 | hebbian       |            12 |          0.9 |              7 |
|  39 |             63 | hebbian       |            12 |          0.6 |             10 |
|  40 |            116 | hebbian       |            23 |          1   |             10 |
|  41 |            116 | hebbian       |            23 |          0.2 |             24 |
|  42 |            116 | hebbian       |            23 |          1   |              6 |
|  43 |            116 | hebbian       |            23 |          0.2 |             24 |
|  44 |            116 | hebbian       |            23 |          1   |              6 |
|  45 |            116 | hebbian       |            23 |          1   |              6 |
|  46 |            116 | hebbian       |            23 |          0.1 |             20 |
|  47 |            116 | hebbian       |            23 |          1   |              8 |
|  48 |            116 | hebbian       |            23 |          0.1 |             24 |
|  49 |            116 | hebbian       |            23 |          1   |              6 |
|  50 |            215 | hebbian       |            43 |          0.4 |             30 |
|  51 |            215 | hebbian       |            43 |          1   |             10 |
|  52 |            215 | hebbian       |            43 |          1   |             13 |
|  53 |            215 | hebbian       |            43 |          1   |             16 |
|  54 |            215 | hebbian       |            43 |          0.7 |             26 |
|  55 |            215 | hebbian       |            43 |          0.5 |             30 |
|  56 |            215 | hebbian       |            43 |          0.6 |             30 |
|  57 |            215 | hebbian       |            43 |          0.9 |             20 |
|  58 |            215 | hebbian       |            43 |          0.5 |             30 |
|  59 |            215 | hebbian       |            43 |          0.7 |             23 |
|  60 |            397 | hebbian       |            79 |          1   |             27 |
|  61 |            397 | hebbian       |            79 |          1   |             38 |
|  62 |            397 | hebbian       |            79 |          0.3 |             44 |
|  63 |            397 | hebbian       |            79 |          1   |             16 |
|  64 |            397 | hebbian       |            79 |          1   |             16 |
|  65 |            397 | hebbian       |            79 |          1   |             16 |
|  66 |            397 | hebbian       |            79 |          0.1 |             60 |
|  67 |            397 | hebbian       |            79 |          0   |             55 |
|  68 |            397 | hebbian       |            79 |          1   |             33 |
|  69 |            397 | hebbian       |            79 |          0.9 |             33 |
|  70 |            733 | hebbian       |           146 |          0.9 |             37 |
|  71 |            733 | hebbian       |           146 |          0.9 |             37 |
|  72 |            733 | hebbian       |           146 |          0.8 |             74 |
|  73 |            733 | hebbian       |           146 |          1   |             37 |
|  74 |            733 | hebbian       |           146 |          1   |             37 |
|  75 |            733 | hebbian       |           146 |          0.7 |             64 |
|  76 |            733 | hebbian       |           146 |          0.2 |             83 |
|  77 |            733 | hebbian       |           146 |          1   |             37 |
|  78 |            733 | hebbian       |           146 |          0.7 |             74 |
|  79 |            733 | hebbian       |           146 |          0.4 |             92 |
|  80 |           1354 | hebbian       |           270 |          1   |             46 |
|  81 |           1354 | hebbian       |           270 |          1   |             93 |
|  82 |           1354 | hebbian       |           270 |          0.7 |            109 |
|  83 |           1354 | hebbian       |           270 |          0   |            156 |
|  84 |           1354 | hebbian       |           270 |          1   |             62 |
|  85 |           1354 | hebbian       |           270 |          0.5 |            125 |
|  86 |           1354 | hebbian       |           270 |          1   |             46 |
|  87 |           1354 | hebbian       |           270 |          1   |             62 |
|  88 |           1354 | hebbian       |           270 |          1   |             78 |
|  89 |           1354 | hebbian       |           270 |          0.1 |            172 |
|  90 |           2500 | hebbian       |           500 |          1   |            106 |
|  91 |           2500 | hebbian       |           500 |          1   |             79 |
|  92 |           2500 | hebbian       |           500 |          0   |            319 |
|  93 |           2500 | hebbian       |           500 |          0   |            319 |
|  94 |           2500 | hebbian       |           500 |          1   |             79 |
|  95 |           2500 | hebbian       |           500 |          0.2 |            239 |
|  96 |           2500 | hebbian       |           500 |          1   |             79 |
|  97 |           2500 | hebbian       |           500 |          0   |            292 |
|  98 |           2500 | hebbian       |           500 |          0.9 |            159 |
|  99 |           2500 | hebbian       |           500 |          1   |            133 |
| 100 |             10 | storkey       |             2 |          0.2 |              6 |
| 101 |             10 | storkey       |             2 |          0.9 |              2 |
| 102 |             10 | storkey       |             2 |          0.2 |              8 |
| 103 |             10 | storkey       |             2 |          0.2 |              6 |
| 104 |             10 | storkey       |             2 |          0.2 |              9 |
| 105 |             10 | storkey       |             2 |          0.3 |              8 |
| 106 |             10 | storkey       |             2 |          0.4 |              6 |
| 107 |             10 | storkey       |             2 |          0.8 |              4 |
| 108 |             10 | storkey       |             2 |          0.3 |              5 |
| 109 |             10 | storkey       |             2 |          0.4 |              7 |
| 110 |             18 | storkey       |             3 |          0   |             13 |
| 111 |             18 | storkey       |             3 |          0.2 |             12 |
| 112 |             18 | storkey       |             3 |          0.3 |             12 |
| 113 |             18 | storkey       |             3 |          0.3 |             11 |
| 114 |             18 | storkey       |             3 |          0   |             13 |
| 115 |             18 | storkey       |             3 |          0.5 |              8 |
| 116 |             18 | storkey       |             3 |          0.6 |              4 |
| 117 |             18 | storkey       |             3 |          0.9 |              3 |
| 118 |             18 | storkey       |             3 |          0   |             13 |
| 119 |             18 | storkey       |             3 |          0.7 |              7 |
| 120 |             34 | storkey       |             6 |          0.2 |             25 |
| 121 |             34 | storkey       |             6 |          0   |             25 |
| 122 |             34 | storkey       |             6 |          0.5 |             14 |
| 123 |             34 | storkey       |             6 |          0.1 |             19 |
| 124 |             34 | storkey       |             6 |          0.7 |             10 |
| 125 |             34 | storkey       |             6 |          0   |             23 |
| 126 |             34 | storkey       |             6 |          0.1 |             21 |
| 127 |             34 | storkey       |             6 |          0   |             21 |
| 128 |             34 | storkey       |             6 |          0.2 |             17 |
| 129 |             34 | storkey       |             6 |          1   |              6 |
| 130 |             63 | storkey       |            12 |          0.2 |             21 |
| 131 |             63 | storkey       |            12 |          0   |             43 |
| 132 |             63 | storkey       |            12 |          0.7 |             21 |
| 133 |             63 | storkey       |            12 |          0   |             40 |
| 134 |             63 | storkey       |            12 |          0.1 |             29 |
| 135 |             63 | storkey       |            12 |          0.7 |             14 |
| 136 |             63 | storkey       |            12 |          0   |             32 |
| 137 |             63 | storkey       |            12 |          0.8 |             14 |
| 138 |             63 | storkey       |            12 |          0   |             43 |
| 139 |             63 | storkey       |            12 |          0.8 |             18 |
| 140 |            116 | storkey       |            23 |          0   |             75 |
| 141 |            116 | storkey       |            23 |          0.9 |             31 |
| 142 |            116 | storkey       |            23 |          1   |             18 |
| 143 |            116 | storkey       |            23 |          0   |             75 |
| 144 |            116 | storkey       |            23 |          0.9 |             25 |
| 145 |            116 | storkey       |            23 |          0   |             50 |
| 146 |            116 | storkey       |            23 |          0   |             75 |
| 147 |            116 | storkey       |            23 |          0   |             62 |
| 148 |            116 | storkey       |            23 |          0.1 |             56 |
| 149 |            116 | storkey       |            23 |          0.2 |             43 |
| 150 |            215 | storkey       |            43 |          0   |             87 |
| 151 |            215 | storkey       |            43 |          0.8 |             54 |
| 152 |            215 | storkey       |            43 |          1   |             32 |
| 153 |            215 | storkey       |            43 |          1   |             32 |
| 154 |            215 | storkey       |            43 |          0   |            120 |
| 155 |            215 | storkey       |            43 |          0   |            109 |
| 156 |            215 | storkey       |            43 |          0   |            120 |
| 157 |            215 | storkey       |            43 |          1   |             32 |
| 158 |            215 | storkey       |            43 |          0.4 |             65 |
| 159 |            215 | storkey       |            43 |          0.8 |             54 |
| 160 |            397 | storkey       |            79 |          0   |            210 |
| 161 |            397 | storkey       |            79 |          0.9 |             95 |
| 162 |            397 | storkey       |            79 |          1   |             57 |
| 163 |            397 | storkey       |            79 |          0.5 |            133 |
| 164 |            397 | storkey       |            79 |          0   |            210 |
| 165 |            397 | storkey       |            79 |          1   |             57 |
| 166 |            397 | storkey       |            79 |          1   |             57 |
| 167 |            397 | storkey       |            79 |          1   |             95 |
| 168 |            397 | storkey       |            79 |          0.1 |            133 |
| 169 |            397 | storkey       |            79 |          1   |             95 |
| 170 |            733 | storkey       |           146 |          0   |            336 |
| 171 |            733 | storkey       |           146 |          0.4 |            235 |
| 172 |            733 | storkey       |           146 |          1   |            100 |
| 173 |            733 | storkey       |           146 |          0   |            336 |
| 174 |            733 | storkey       |           146 |          0.1 |            269 |
| 175 |            733 | storkey       |           146 |          0.1 |            269 |
| 176 |            733 | storkey       |           146 |          0   |            336 |
| 177 |            733 | storkey       |           146 |          0.1 |            269 |
| 178 |            733 | storkey       |           146 |          0   |            403 |
| 179 |            733 | storkey       |           146 |          0.6 |            201 |
| 180 |           1354 | storkey       |           270 |          0.6 |            415 |
| 181 |           1354 | storkey       |           270 |          0   |            713 |
| 182 |           1354 | storkey       |           270 |          1   |            178 |
| 183 |           1354 | storkey       |           270 |          0   |            653 |
| 184 |           1354 | storkey       |           270 |          0   |            653 |
| 185 |           1354 | storkey       |           270 |          0   |            713 |
| 186 |           1354 | storkey       |           270 |          1   |            297 |
| 187 |           1354 | storkey       |           270 |          1   |            356 |
| 188 |           1354 | storkey       |           270 |          0.6 |            415 |
| 189 |           1354 | storkey       |           270 |          1   |            178 |
| 190 |           2500 | storkey       |           500 |          1   |            315 |
| 191 |           2500 | storkey       |           500 |          0   |           1158 |
| 192 |           2500 | storkey       |           500 |          0.7 |            737 |
| 193 |           2500 | storkey       |           500 |          1   |            315 |
| 194 |           2500 | storkey       |           500 |          0   |           1053 |
| 195 |           2500 | storkey       |           500 |          0.6 |            737 |
| 196 |           2500 | storkey       |           500 |          0.7 |            737 |
| 197 |           2500 | storkey       |           500 |          0   |            947 |
| 198 |           2500 | storkey       |           500 |          0   |           1158 |
| 199 |           2500 | storkey       |           500 |          0.3 |            842 |



<h2 align="center"> 2. Robustness Plots
</h2>

### Hebbian plots

 ![hebbian_robustness_of_size_10](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_10.png)

 ![hebbian_robustness_of_size_18](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_18.png)

![hebbian_robustness_of_size_34](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_34.png)

![hebbian_robustness_of_size_63](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_63.png)

![hebbian_robustness_of_size_1116](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_116.png)

![hebbian_robustness_of_size_215](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_215.png)

![hebbian_robustness_of_size_397](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_397.png)

![hebbian_robustness_of_size_733](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_733.png)

![hebbian_robustness_of_size_1354](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_1354.png)

![hebbian_robustness_of_size_2500](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/hebbian_robustness_of_size_2500.png)

### Storkey Plots

![storkey_robustness_of_size_10](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_10.png)

![storkey_robustness_of_size_18](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_18.png)

![storkey_robustness_of_size_34](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_34.png)

![storkey_robustness_of_size_63](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_63.png)

![storkey_robustness_of_size_1116](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_116.png)

![storkey_robustness_of_size_215](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_215.png)

![storkey_robustness_of_size_397](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_397.png)

![storkey_robustness_of_size_733](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_733.png)

![storkey_robustness_of_size_1354](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_1354.png)

![storkey_robustness_of_size_2500](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Exp_Data/Robustness_Graphs/storkey_robustness_of_size_2500.png)

<h2 align="center"> Robustness table
</h2>

|     |   network_size | weight_rule   |   num perturb |   match_frac |   num_patterns |
|----:|---------------:|:--------------|--------------:|-------------:|---------------:|
|   0 |             10 | hebbian       |             0 |          1   |              2 |
|   1 |             10 | hebbian       |             0 |          1   |              2 |
|   2 |             10 | hebbian       |             1 |          1   |              2 |
|   3 |             10 | hebbian       |             1 |          0.9 |              2 |
|   4 |             10 | hebbian       |             2 |          0.9 |              2 |
|   5 |             10 | hebbian       |             2 |          0.8 |              2 |
|   6 |             10 | hebbian       |             3 |          0.6 |              2 |
|   7 |             10 | hebbian       |             3 |          0.6 |              2 |
|   8 |             10 | hebbian       |             4 |          0.5 |              2 |
|   9 |             10 | hebbian       |             4 |          0.5 |              2 |
|  10 |             10 | hebbian       |             5 |          0.3 |              2 |
|  11 |             10 | hebbian       |             5 |          0.2 |              2 |
|  12 |             10 | hebbian       |             6 |          0.1 |              2 |
|  13 |             10 | hebbian       |             6 |          0.2 |              2 |
|  14 |             10 | hebbian       |             7 |          0.1 |              2 |
|  15 |             10 | hebbian       |             7 |          0   |              2 |
|  16 |             10 | hebbian       |             8 |          0.1 |              2 |
|  17 |             10 | hebbian       |             8 |          0   |              2 |
|  18 |             10 | hebbian       |             9 |          0   |              2 |
|  19 |             10 | hebbian       |             9 |          0   |              2 |
|  20 |             18 | hebbian       |             0 |          1   |              2 |
|  21 |             18 | hebbian       |             0 |          1   |              2 |
|  22 |             18 | hebbian       |             1 |          1   |              2 |
|  23 |             18 | hebbian       |             2 |          1   |              2 |
|  24 |             18 | hebbian       |             3 |          1   |              2 |
|  25 |             18 | hebbian       |             4 |          0.9 |              2 |
|  26 |             18 | hebbian       |             5 |          0.9 |              2 |
|  27 |             18 | hebbian       |             6 |          0.8 |              2 |
|  28 |             18 | hebbian       |             7 |          0.6 |              2 |
|  29 |             18 | hebbian       |             8 |          0.6 |              2 |
|  30 |             18 | hebbian       |             9 |          0.5 |              2 |
|  31 |             18 | hebbian       |             9 |          0.4 |              2 |
|  32 |             18 | hebbian       |            10 |          0.4 |              2 |
|  33 |             18 | hebbian       |            11 |          0   |              2 |
|  34 |             18 | hebbian       |            12 |          0.1 |              2 |
|  35 |             18 | hebbian       |            13 |          0   |              2 |
|  36 |             18 | hebbian       |            14 |          0   |              2 |
|  37 |             18 | hebbian       |            15 |          0   |              2 |
|  38 |             18 | hebbian       |            16 |          0   |              2 |
|  39 |             18 | hebbian       |            17 |          0   |              2 |
|  40 |             34 | hebbian       |             0 |          1   |              2 |
|  41 |             34 | hebbian       |             1 |          1   |              2 |
|  42 |             34 | hebbian       |             3 |          1   |              2 |
|  43 |             34 | hebbian       |             5 |          1   |              2 |
|  44 |             34 | hebbian       |             6 |          1   |              2 |
|  45 |             34 | hebbian       |             8 |          1   |              2 |
|  46 |             34 | hebbian       |            10 |          0.9 |              2 |
|  47 |             34 | hebbian       |            11 |          1   |              2 |
|  48 |             34 | hebbian       |            13 |          0.7 |              2 |
|  49 |             34 | hebbian       |            15 |          0.6 |              2 |
|  50 |             34 | hebbian       |            17 |          0.5 |              2 |
|  51 |             34 | hebbian       |            18 |          0.3 |              2 |
|  52 |             34 | hebbian       |            20 |          0   |              2 |
|  53 |             34 | hebbian       |            22 |          0   |              2 |
|  54 |             34 | hebbian       |            23 |          0   |              2 |
|  55 |             34 | hebbian       |            25 |          0   |              2 |
|  56 |             34 | hebbian       |            27 |          0   |              2 |
|  57 |             34 | hebbian       |            28 |          0   |              2 |
|  58 |             34 | hebbian       |            30 |          0   |              2 |
|  59 |             34 | hebbian       |            32 |          0   |              2 |
|  60 |             63 | hebbian       |             0 |          1   |              2 |
|  61 |             63 | hebbian       |             3 |          1   |              2 |
|  62 |             63 | hebbian       |             6 |          1   |              2 |
|  63 |             63 | hebbian       |             9 |          1   |              2 |
|  64 |             63 | hebbian       |            12 |          1   |              2 |
|  65 |             63 | hebbian       |            15 |          1   |              2 |
|  66 |             63 | hebbian       |            18 |          1   |              2 |
|  67 |             63 | hebbian       |            22 |          1   |              2 |
|  68 |             63 | hebbian       |            25 |          0.9 |              2 |
|  69 |             63 | hebbian       |            28 |          0.6 |              2 |
|  70 |             63 | hebbian       |            31 |          0.4 |              2 |
|  71 |             63 | hebbian       |            34 |          0.1 |              2 |
|  72 |             63 | hebbian       |            37 |          0.1 |              2 |
|  73 |             63 | hebbian       |            40 |          0   |              2 |
|  74 |             63 | hebbian       |            44 |          0   |              2 |
|  75 |             63 | hebbian       |            47 |          0   |              2 |
|  76 |             63 | hebbian       |            50 |          0   |              2 |
|  77 |             63 | hebbian       |            53 |          0   |              2 |
|  78 |             63 | hebbian       |            56 |          0   |              2 |
|  79 |             63 | hebbian       |            59 |          0   |              2 |
|  80 |            116 | hebbian       |             0 |          1   |              2 |
|  81 |            116 | hebbian       |             5 |          1   |              2 |
|  82 |            116 | hebbian       |            11 |          1   |              2 |
|  83 |            116 | hebbian       |            17 |          1   |              2 |
|  84 |            116 | hebbian       |            23 |          1   |              2 |
|  85 |            116 | hebbian       |            29 |          1   |              2 |
|  86 |            116 | hebbian       |            34 |          1   |              2 |
|  87 |            116 | hebbian       |            40 |          1   |              2 |
|  88 |            116 | hebbian       |            46 |          0.9 |              2 |
|  89 |            116 | hebbian       |            52 |          0.8 |              2 |
|  90 |            116 | hebbian       |            58 |          0.5 |              2 |
|  91 |            116 | hebbian       |            63 |          0.2 |              2 |
|  92 |            116 | hebbian       |            69 |          0   |              2 |
|  93 |            116 | hebbian       |            75 |          0   |              2 |
|  94 |            116 | hebbian       |            81 |          0   |              2 |
|  95 |            116 | hebbian       |            87 |          0   |              2 |
|  96 |            116 | hebbian       |            92 |          0   |              2 |
|  97 |            116 | hebbian       |            98 |          0   |              2 |
|  98 |            116 | hebbian       |           104 |          0   |              2 |
|  99 |            116 | hebbian       |           110 |          0   |              2 |
| 100 |            215 | hebbian       |             0 |          1   |              2 |
| 101 |            215 | hebbian       |            10 |          1   |              2 |
| 102 |            215 | hebbian       |            21 |          1   |              2 |
| 103 |            215 | hebbian       |            32 |          1   |              2 |
| 104 |            215 | hebbian       |            43 |          1   |              2 |
| 105 |            215 | hebbian       |            53 |          1   |              2 |
| 106 |            215 | hebbian       |            64 |          1   |              2 |
| 107 |            215 | hebbian       |            75 |          1   |              2 |
| 108 |            215 | hebbian       |            86 |          1   |              2 |
| 109 |            215 | hebbian       |            96 |          0.9 |              2 |
| 110 |            215 | hebbian       |           107 |          0.5 |              2 |
| 111 |            215 | hebbian       |           118 |          0   |              2 |
| 112 |            215 | hebbian       |           129 |          0   |              2 |
| 113 |            215 | hebbian       |           139 |          0   |              2 |
| 114 |            215 | hebbian       |           150 |          0   |              2 |
| 115 |            215 | hebbian       |           161 |          0   |              2 |
| 116 |            215 | hebbian       |           172 |          0   |              2 |
| 117 |            215 | hebbian       |           182 |          0   |              2 |
| 118 |            215 | hebbian       |           193 |          0   |              2 |
| 119 |            215 | hebbian       |           204 |          0   |              2 |
| 120 |            397 | hebbian       |             0 |          1   |              2 |
| 121 |            397 | hebbian       |            19 |          1   |              2 |
| 122 |            397 | hebbian       |            39 |          1   |              2 |
| 123 |            397 | hebbian       |            59 |          1   |              2 |
| 124 |            397 | hebbian       |            79 |          1   |              2 |
| 125 |            397 | hebbian       |            99 |          1   |              2 |
| 126 |            397 | hebbian       |           119 |          1   |              2 |
| 127 |            397 | hebbian       |           138 |          1   |              2 |
| 128 |            397 | hebbian       |           158 |          1   |              2 |
| 129 |            397 | hebbian       |           178 |          1   |              2 |
| 130 |            397 | hebbian       |           198 |          0.4 |              2 |
| 131 |            397 | hebbian       |           218 |          0.1 |              2 |
| 132 |            397 | hebbian       |           238 |          0   |              2 |
| 133 |            397 | hebbian       |           258 |          0   |              2 |
| 134 |            397 | hebbian       |           277 |          0   |              2 |
| 135 |            397 | hebbian       |           297 |          0   |              2 |
| 136 |            397 | hebbian       |           317 |          0   |              2 |
| 137 |            397 | hebbian       |           337 |          0   |              2 |
| 138 |            397 | hebbian       |           357 |          0   |              2 |
| 139 |            397 | hebbian       |           377 |          0   |              2 |
| 140 |            733 | hebbian       |             0 |          1   |              2 |
| 141 |            733 | hebbian       |            36 |          1   |              2 |
| 142 |            733 | hebbian       |            73 |          1   |              2 |
| 143 |            733 | hebbian       |           109 |          1   |              2 |
| 144 |            733 | hebbian       |           146 |          1   |              2 |
| 145 |            733 | hebbian       |           183 |          1   |              2 |
| 146 |            733 | hebbian       |           219 |          1   |              2 |
| 147 |            733 | hebbian       |           256 |          1   |              2 |
| 148 |            733 | hebbian       |           293 |          1   |              2 |
| 149 |            733 | hebbian       |           329 |          1   |              2 |
| 150 |            733 | hebbian       |           366 |          0.3 |              2 |
| 151 |            733 | hebbian       |           403 |          0   |              2 |
| 152 |            733 | hebbian       |           439 |          0   |              2 |
| 153 |            733 | hebbian       |           476 |          0   |              2 |
| 154 |            733 | hebbian       |           513 |          0   |              2 |
| 155 |            733 | hebbian       |           549 |          0   |              2 |
| 156 |            733 | hebbian       |           586 |          0   |              2 |
| 157 |            733 | hebbian       |           623 |          0   |              2 |
| 158 |            733 | hebbian       |           659 |          0   |              2 |
| 159 |            733 | hebbian       |           696 |          0   |              2 |
| 160 |           1354 | hebbian       |             0 |          1   |              2 |
| 161 |           1354 | hebbian       |            67 |          1   |              2 |
| 162 |           1354 | hebbian       |           135 |          1   |              2 |
| 163 |           1354 | hebbian       |           203 |          1   |              2 |
| 164 |           1354 | hebbian       |           270 |          1   |              2 |
| 165 |           1354 | hebbian       |           338 |          1   |              2 |
| 166 |           1354 | hebbian       |           406 |          1   |              2 |
| 167 |           1354 | hebbian       |           473 |          1   |              2 |
| 168 |           1354 | hebbian       |           541 |          1   |              2 |
| 169 |           1354 | hebbian       |           609 |          1   |              2 |
| 170 |           1354 | hebbian       |           677 |          0.4 |              2 |
| 171 |           1354 | hebbian       |           744 |          0   |              2 |
| 172 |           1354 | hebbian       |           812 |          0   |              2 |
| 173 |           1354 | hebbian       |           880 |          0   |              2 |
| 174 |           1354 | hebbian       |           947 |          0   |              2 |
| 175 |           1354 | hebbian       |          1015 |          0   |              2 |
| 176 |           1354 | hebbian       |          1083 |          0   |              2 |
| 177 |           1354 | hebbian       |          1150 |          0   |              2 |
| 178 |           1354 | hebbian       |          1218 |          0   |              2 |
| 179 |           1354 | hebbian       |          1286 |          0   |              2 |
| 180 |           2500 | hebbian       |             0 |          1   |              2 |
| 181 |           2500 | hebbian       |           125 |          1   |              2 |
| 182 |           2500 | hebbian       |           250 |          1   |              2 |
| 183 |           2500 | hebbian       |           375 |          1   |              2 |
| 184 |           2500 | hebbian       |           500 |          1   |              2 |
| 185 |           2500 | hebbian       |           625 |          1   |              2 |
| 186 |           2500 | hebbian       |           750 |          1   |              2 |
| 187 |           2500 | hebbian       |           875 |          1   |              2 |
| 188 |           2500 | hebbian       |          1000 |          1   |              2 |
| 189 |           2500 | hebbian       |          1125 |          1   |              2 |
| 190 |           2500 | hebbian       |          1250 |          0.6 |              2 |
| 191 |           2500 | hebbian       |          1375 |          0   |              2 |
| 192 |           2500 | hebbian       |          1500 |          0   |              2 |
| 193 |           2500 | hebbian       |          1625 |          0   |              2 |
| 194 |           2500 | hebbian       |          1750 |          0   |              2 |
| 195 |           2500 | hebbian       |          1875 |          0   |              2 |
| 196 |           2500 | hebbian       |          2000 |          0   |              2 |
| 197 |           2500 | hebbian       |          2125 |          0   |              2 |
| 198 |           2500 | hebbian       |          2250 |          0   |              2 |
| 199 |           2500 | hebbian       |          2375 |          0   |              2 |
| 200 |             10 | storkey       |             0 |          1   |              2 |
| 201 |             10 | storkey       |             0 |          1   |              2 |
| 202 |             10 | storkey       |             1 |          1   |              2 |
| 203 |             10 | storkey       |             1 |          1   |              2 |
| 204 |             10 | storkey       |             2 |          0.7 |              2 |
| 205 |             10 | storkey       |             2 |          1   |              2 |
| 206 |             10 | storkey       |             3 |          0.8 |              2 |
| 207 |             10 | storkey       |             3 |          0.6 |              2 |
| 208 |             10 | storkey       |             4 |          0.3 |              2 |
| 209 |             10 | storkey       |             4 |          0.5 |              2 |
| 210 |             10 | storkey       |             5 |          0.3 |              2 |
| 211 |             10 | storkey       |             5 |          0.1 |              2 |
| 212 |             10 | storkey       |             6 |          0.3 |              2 |
| 213 |             10 | storkey       |             6 |          0.4 |              2 |
| 214 |             10 | storkey       |             7 |          0.2 |              2 |
| 215 |             10 | storkey       |             7 |          0.1 |              2 |
| 216 |             10 | storkey       |             8 |          0   |              2 |
| 217 |             10 | storkey       |             8 |          0   |              2 |
| 218 |             10 | storkey       |             9 |          0.1 |              2 |
| 219 |             10 | storkey       |             9 |          0   |              2 |
| 220 |             18 | storkey       |             0 |          1   |              2 |
| 221 |             18 | storkey       |             0 |          1   |              2 |
| 222 |             18 | storkey       |             1 |          1   |              2 |
| 223 |             18 | storkey       |             2 |          1   |              2 |
| 224 |             18 | storkey       |             3 |          1   |              2 |
| 225 |             18 | storkey       |             4 |          1   |              2 |
| 226 |             18 | storkey       |             5 |          1   |              2 |
| 227 |             18 | storkey       |             6 |          0.8 |              2 |
| 228 |             18 | storkey       |             7 |          0.4 |              2 |
| 229 |             18 | storkey       |             8 |          0.4 |              2 |
| 230 |             18 | storkey       |             9 |          0.4 |              2 |
| 231 |             18 | storkey       |             9 |          0.5 |              2 |
| 232 |             18 | storkey       |            10 |          0.3 |              2 |
| 233 |             18 | storkey       |            11 |          0.2 |              2 |
| 234 |             18 | storkey       |            12 |          0.2 |              2 |
| 235 |             18 | storkey       |            13 |          0   |              2 |
| 236 |             18 | storkey       |            14 |          0   |              2 |
| 237 |             18 | storkey       |            15 |          0   |              2 |
| 238 |             18 | storkey       |            16 |          0   |              2 |
| 239 |             18 | storkey       |            17 |          0   |              2 |
| 240 |             34 | storkey       |             0 |          1   |              2 |
| 241 |             34 | storkey       |             1 |          1   |              2 |
| 242 |             34 | storkey       |             3 |          1   |              2 |
| 243 |             34 | storkey       |             5 |          1   |              2 |
| 244 |             34 | storkey       |             6 |          1   |              2 |
| 245 |             34 | storkey       |             8 |          1   |              2 |
| 246 |             34 | storkey       |            10 |          1   |              2 |
| 247 |             34 | storkey       |            11 |          1   |              2 |
| 248 |             34 | storkey       |            13 |          0.6 |              2 |
| 249 |             34 | storkey       |            15 |          0.5 |              2 |
| 250 |             34 | storkey       |            17 |          0.4 |              2 |
| 251 |             34 | storkey       |            18 |          0.2 |              2 |
| 252 |             34 | storkey       |            20 |          0.3 |              2 |
| 253 |             34 | storkey       |            22 |          0   |              2 |
| 254 |             34 | storkey       |            23 |          0   |              2 |
| 255 |             34 | storkey       |            25 |          0   |              2 |
| 256 |             34 | storkey       |            27 |          0   |              2 |
| 257 |             34 | storkey       |            28 |          0   |              2 |
| 258 |             34 | storkey       |            30 |          0   |              2 |
| 259 |             34 | storkey       |            32 |          0   |              2 |
| 260 |             63 | storkey       |             0 |          1   |              2 |
| 261 |             63 | storkey       |             3 |          1   |              2 |
| 262 |             63 | storkey       |             6 |          1   |              2 |
| 263 |             63 | storkey       |             9 |          1   |              2 |
| 264 |             63 | storkey       |            12 |          1   |              2 |
| 265 |             63 | storkey       |            15 |          1   |              2 |
| 266 |             63 | storkey       |            18 |          1   |              2 |
| 267 |             63 | storkey       |            22 |          0.9 |              2 |
| 268 |             63 | storkey       |            25 |          0.9 |              2 |
| 269 |             63 | storkey       |            28 |          0.8 |              2 |
| 270 |             63 | storkey       |            31 |          0.3 |              2 |
| 271 |             63 | storkey       |            34 |          0.3 |              2 |
| 272 |             63 | storkey       |            37 |          0   |              2 |
| 273 |             63 | storkey       |            40 |          0   |              2 |
| 274 |             63 | storkey       |            44 |          0   |              2 |
| 275 |             63 | storkey       |            47 |          0   |              2 |
| 276 |             63 | storkey       |            50 |          0   |              2 |
| 277 |             63 | storkey       |            53 |          0   |              2 |
| 278 |             63 | storkey       |            56 |          0   |              2 |
| 279 |             63 | storkey       |            59 |          0   |              2 |
| 280 |            116 | storkey       |             0 |          1   |              2 |
| 281 |            116 | storkey       |             5 |          1   |              2 |
| 282 |            116 | storkey       |            11 |          1   |              2 |
| 283 |            116 | storkey       |            17 |          1   |              2 |
| 284 |            116 | storkey       |            23 |          1   |              2 |
| 285 |            116 | storkey       |            29 |          1   |              2 |
| 286 |            116 | storkey       |            34 |          1   |              2 |
| 287 |            116 | storkey       |            40 |          1   |              2 |
| 288 |            116 | storkey       |            46 |          0.9 |              2 |
| 289 |            116 | storkey       |            52 |          0.7 |              2 |
| 290 |            116 | storkey       |            58 |          0.6 |              2 |
| 291 |            116 | storkey       |            63 |          0.2 |              2 |
| 292 |            116 | storkey       |            69 |          0   |              2 |
| 293 |            116 | storkey       |            75 |          0   |              2 |
| 294 |            116 | storkey       |            81 |          0   |              2 |
| 295 |            116 | storkey       |            87 |          0   |              2 |
| 296 |            116 | storkey       |            92 |          0   |              2 |
| 297 |            116 | storkey       |            98 |          0   |              2 |
| 298 |            116 | storkey       |           104 |          0   |              2 |
| 299 |            116 | storkey       |           110 |          0   |              2 |
| 300 |            215 | storkey       |             0 |          1   |              2 |
| 301 |            215 | storkey       |            10 |          1   |              2 |
| 302 |            215 | storkey       |            21 |          1   |              2 |
| 303 |            215 | storkey       |            32 |          1   |              2 |
| 304 |            215 | storkey       |            43 |          1   |              2 |
| 305 |            215 | storkey       |            53 |          1   |              2 |
| 306 |            215 | storkey       |            64 |          1   |              2 |
| 307 |            215 | storkey       |            75 |          1   |              2 |
| 308 |            215 | storkey       |            86 |          1   |              2 |
| 309 |            215 | storkey       |            96 |          1   |              2 |
| 310 |            215 | storkey       |           107 |          0.1 |              2 |
| 311 |            215 | storkey       |           118 |          0.1 |              2 |
| 312 |            215 | storkey       |           129 |          0   |              2 |
| 313 |            215 | storkey       |           139 |          0   |              2 |
| 314 |            215 | storkey       |           150 |          0   |              2 |
| 315 |            215 | storkey       |           161 |          0   |              2 |
| 316 |            215 | storkey       |           172 |          0   |              2 |
| 317 |            215 | storkey       |           182 |          0   |              2 |
| 318 |            215 | storkey       |           193 |          0   |              2 |
| 319 |            215 | storkey       |           204 |          0   |              2 |
| 320 |            397 | storkey       |             0 |          1   |              2 |
| 321 |            397 | storkey       |            19 |          1   |              2 |
| 322 |            397 | storkey       |            39 |          1   |              2 |
| 323 |            397 | storkey       |            59 |          1   |              2 |
| 324 |            397 | storkey       |            79 |          1   |              2 |
| 325 |            397 | storkey       |            99 |          1   |              2 |
| 326 |            397 | storkey       |           119 |          1   |              2 |
| 327 |            397 | storkey       |           138 |          1   |              2 |
| 328 |            397 | storkey       |           158 |          1   |              2 |
| 329 |            397 | storkey       |           178 |          1   |              2 |
| 330 |            397 | storkey       |           198 |          0.3 |              2 |
| 331 |            397 | storkey       |           218 |          0.1 |              2 |
| 332 |            397 | storkey       |           238 |          0   |              2 |
| 333 |            397 | storkey       |           258 |          0   |              2 |
| 334 |            397 | storkey       |           277 |          0   |              2 |
| 335 |            397 | storkey       |           297 |          0   |              2 |
| 336 |            397 | storkey       |           317 |          0   |              2 |
| 337 |            397 | storkey       |           337 |          0   |              2 |
| 338 |            397 | storkey       |           357 |          0   |              2 |
| 339 |            397 | storkey       |           377 |          0   |              2 |
| 340 |            733 | storkey       |             0 |          1   |              2 |
| 341 |            733 | storkey       |            36 |          1   |              2 |
| 342 |            733 | storkey       |            73 |          1   |              2 |
| 343 |            733 | storkey       |           109 |          1   |              2 |
| 344 |            733 | storkey       |           146 |          1   |              2 |
| 345 |            733 | storkey       |           183 |          1   |              2 |
| 346 |            733 | storkey       |           219 |          1   |              2 |
| 347 |            733 | storkey       |           256 |          1   |              2 |
| 348 |            733 | storkey       |           293 |          1   |              2 |
| 349 |            733 | storkey       |           329 |          1   |              2 |
| 350 |            733 | storkey       |           366 |          0.6 |              2 |
| 351 |            733 | storkey       |           403 |          0   |              2 |
| 352 |            733 | storkey       |           439 |          0   |              2 |
| 353 |            733 | storkey       |           476 |          0   |              2 |
| 354 |            733 | storkey       |           513 |          0   |              2 |
| 355 |            733 | storkey       |           549 |          0   |              2 |
| 356 |            733 | storkey       |           586 |          0   |              2 |
| 357 |            733 | storkey       |           623 |          0   |              2 |
| 358 |            733 | storkey       |           659 |          0   |              2 |
| 359 |            733 | storkey       |           696 |          0   |              2 |
| 360 |           1354 | storkey       |             0 |          1   |              2 |
| 361 |           1354 | storkey       |            67 |          1   |              2 |
| 362 |           1354 | storkey       |           135 |          1   |              2 |
| 363 |           1354 | storkey       |           203 |          1   |              2 |
| 364 |           1354 | storkey       |           270 |          1   |              2 |
| 365 |           1354 | storkey       |           338 |          1   |              2 |
| 366 |           1354 | storkey       |           406 |          1   |              2 |
| 367 |           1354 | storkey       |           473 |          1   |              2 |
| 368 |           1354 | storkey       |           541 |          1   |              2 |
| 369 |           1354 | storkey       |           609 |          1   |              2 |
| 370 |           1354 | storkey       |           677 |          0.4 |              2 |
| 371 |           1354 | storkey       |           744 |          0   |              2 |
| 372 |           1354 | storkey       |           812 |          0   |              2 |
| 373 |           1354 | storkey       |           880 |          0   |              2 |
| 374 |           1354 | storkey       |           947 |          0   |              2 |
| 375 |           1354 | storkey       |          1015 |          0   |              2 |
| 376 |           1354 | storkey       |          1083 |          0   |              2 |
| 377 |           1354 | storkey       |          1150 |          0   |              2 |
| 378 |           1354 | storkey       |          1218 |          0   |              2 |
| 379 |           1354 | storkey       |          1286 |          0   |              2 |
| 380 |           2500 | storkey       |             0 |          1   |              2 |
| 381 |           2500 | storkey       |           125 |          1   |              2 |
| 382 |           2500 | storkey       |           250 |          1   |              2 |
| 383 |           2500 | storkey       |           375 |          1   |              2 |
| 384 |           2500 | storkey       |           500 |          1   |              2 |
| 385 |           2500 | storkey       |           625 |          1   |              2 |
| 386 |           2500 | storkey       |           750 |          1   |              2 |
| 387 |           2500 | storkey       |           875 |          1   |              2 |
| 388 |           2500 | storkey       |          1000 |          1   |              2 |
| 389 |           2500 | storkey       |          1125 |          1   |              2 |
| 390 |           2500 | storkey       |          1250 |          0.6 |              2 |
| 391 |           2500 | storkey       |          1375 |          0   |              2 |
| 392 |           2500 | storkey       |          1500 |          0   |              2 |
| 393 |           2500 | storkey       |          1625 |          0   |              2 |
| 394 |           2500 | storkey       |          1750 |          0   |              2 |
| 395 |           2500 | storkey       |          1875 |          0   |              2 |
| 396 |           2500 | storkey       |          2000 |          0   |              2 |
| 397 |           2500 | storkey       |          2125 |          0   |              2 |
| 398 |           2500 | storkey       |          2250 |          0   |              2 |
| 399 |           2500 | storkey       |          2375 |          0   |              2 |


<h2 align="center"> 3. Recall of corrumpted image
</h2>

Here is the yoshi image before being binarized:

![Yoshi_png_1](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Images/yoshi.png)

Here is the yoshi image after being binarized:

![Yoshi_png_2](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Images/Yoshi_after_bin.png)

Here is the yoshi image during recall using asynchronous dynamics with the hebbian rule:

![Yoshi_png_3](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Images/Yoshi_during_retreival.png)

Here is the yoshi image after recall:


![Yoshi_png_4](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Images/Yoshi_after_recall.png)

[Video of recall of corrupted yoshi image](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/Visuals/Videos/asynchronous_hebbian_Yoshi_video.mp4)

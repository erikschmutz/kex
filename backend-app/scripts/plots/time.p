set terminal png
set output "combined.png"
set title "Train model benchmark"
set key right center
set xlabel "# Images"
set ylabel "Execution time (s)"

plot "train_relu_adam_200_1e-2.dat" u 1:2 w linespoints title "AMD Ryzen 7", \
"train_relu_adam_200_1e-4.dat" u 1:2 w linespoints title "Intel I7"

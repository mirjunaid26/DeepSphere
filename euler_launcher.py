import os

cmd = 'bsub -W 48:00 -n 36 -R "rusage[mem=2000]" -R fullnode -oo log_{0}-{1}-{2}.txt python results_psd_with_augmentation.py {0} {1} {2}'

def launch_simulation(sigma, order, sigma_noise):
    sbatch_txt = txtfile.format(sigma, order, sigma_noise)
    os.system(cmd.format(sigma, order, sigma_noise))


sigma = 3
orders = [1, 2, 4]
if sigma == 3:
    sigma_noises = [0, 0.5, 1, 1.5, 2]
else:
    sigma_noises = [1, 2, 3, 4, 5]
for order in orders:
    for sigma_noise in sigma_noises:
        launch_simulation(sigma, order, sigma_noise)
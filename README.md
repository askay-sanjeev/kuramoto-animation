# kuramoto-animation
Mean-fiedl model is described by:

$$ \dot{\theta_i} = \omega_i + Kr\sum_{i=1}^N \sin(\theta_i -\theta_j)$$

To make it more visually apealing I have added an additive noise term as well. 

$$ \dot{\theta_i} = \omega_i + \sum_{i=1}^N K_{ij} \sin(\theta_i -\theta_j)+ \zeta(t)$$

The order parameter, $r$ is calculated from
 
$$ re^{i \psi} = \frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j}$$

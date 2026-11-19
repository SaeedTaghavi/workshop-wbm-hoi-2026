import numpy as np
from scipy.stats import norm
from scipy.special import psi


def gaussian_ent_biascorr(N, T):
    """Bias corrector of the Gaussian entropy estimator (N dims, T samples)."""
    return 0.5 * (N * np.log(2 / (T - 1)) + np.sum(psi((T - np.arange(1, N + 1)) / 2)))


def multi_fc(data):
    """
    O-information matrix (pairwise MI - CMI given the rest) with Gaussian copula.

    Same result as the pairwise-loop version, in closed form:
        MI_ij  = -0.5 log(1 - rho_ij^2) + bc2 - 2 bc1
        CMI_ij = -0.5 log(1 - r_ij^2)   + bcN + bcN-2 - 2 bcN-1
    rho_ij : correlation (from the covariance matrix)
    r_ij   : partial correlation (from the precision matrix P = cov^-1),
             r_ij = -P_ij / sqrt(P_ii P_jj)

    data : (T, N) array. Returns omat : (N, N), zero diagonal.
    """
    T, N = data.shape

    # Gaussian copula (rank -> uniform -> standard normal)
    copdata = (np.argsort(np.argsort(data, axis=0), axis=0) + 1) / (T + 1)
    gaussian_data = norm.ppf(copdata)
    gaussian_data[np.isinf(gaussian_data)] = 0

    # GC covariance and precision matrices
    gc_covmat = (gaussian_data.T @ gaussian_data) / (T - 1)
    gc_precmat = np.linalg.inv(gc_covmat)

    # correlation and partial correlation
    d = np.sqrt(np.diag(gc_covmat))
    rho = gc_covmat / np.outer(d, d)
    dp = np.sqrt(np.diag(gc_precmat))
    pcorr = -gc_precmat / np.outer(dp, dp)
    np.fill_diagonal(rho, 0)
    np.fill_diagonal(pcorr, 0)

    bc = lambda n: gaussian_ent_biascorr(n, T)
    mimat = -0.5 * np.log1p(-rho**2) + bc(2) - 2 * bc(1)
    cmimat = -0.5 * np.log1p(-pcorr**2) + bc(N) + bc(N - 2) - 2 * bc(N - 1)

    omat = mimat - cmimat
    np.fill_diagonal(omat, 0)
    return omat

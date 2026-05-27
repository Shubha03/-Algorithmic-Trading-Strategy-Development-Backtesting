from walk_forward.walk_forward_analysis import (
    average_wfa_score
)


def normalize_wfa(score):

    return max(
        70,
        min(score, 100)
    )


consistency_score = 88

parameter_stability_score = 85

wfa_score = normalize_wfa(
    average_wfa_score
)

robustness_score = (

    0.40 * consistency_score

    + 0.30 * parameter_stability_score

    + 0.30 * wfa_score
)
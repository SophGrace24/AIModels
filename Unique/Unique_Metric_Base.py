"""
Name: Unique_Metric_Base.py

"""

def generateBalancedProfile(profileA, profileB, dimensions,
                              weightA, weightB,
                              minScore=0.0, maxScore=1.0):
    # ... (Input Validations)
    if not isinstance(profileA, dict) or not isinstance(profileB, dict):
        raise TypeError("profileA and profileB must be dictionaries.")
    if not isinstance(dimensions, list):
        raise TypeError("dimensions must be a list.")
    if not dimensions:
        raise ValueError("dimensions list cannot be empty.")
    if not all(isinstance(dim, str) for dim in dimensions):
        raise TypeError("All items in dimensions list must be strings.")
    if not isinstance(weightA, (int, float)) or not isinstance(weightB, (int, float)):
        raise TypeError("weightA and weightB must be numbers.")
    if abs((weightA + weightB) - 1.0) > 1e-9:
        raise ValueError(f"Weights must sum to 1.0. Current sum: {weightA + weightB}")
    if not isinstance(minScore, (int, float)) or not isinstance(maxScore, (int, float)):
        raise TypeError("minScore and maxScore must be numbers.")
    if minScore >= maxScore:
        raise ValueError("minScore must be less than maxScore.")

    # --- Initialize Result Structure ---
    result = {
        'balancedProfile': {},
        'appliedWeights': {'profileA': weightA, 'profileB': weightB},
        'clippingActivity': []
    }

    # --- Profile Calculation ---
    for dim in dimensions:
        scoreA = profileA.get(dim)
        scoreB = profileB.get(dim)

        if not isinstance(scoreA, (int, float)):
            raise TypeError(f"Score for dimension '{dim}' in profileA is not a number: {scoreA}")
        if not isinstance(scoreB, (int, float)):
            raise TypeError(f"Score for dimension '{dim}' in profileB is not a number: {scoreB}")

        clippedScoreA = max(minScore, min(scoreA, maxScore))
        clippedScoreB = max(minScore, min(scoreB, maxScore))

        if clippedScoreA != scoreA:
            result['clippingActivity'].append(
                f"Dimension '{dim}': profileA score ({scoreA}) clipped to {clippedScoreA} (range: {minScore}-{maxScore})."
            )
        if clippedScoreB != scoreB:
            result['clippingActivity'].append(
                f"Dimension '{dim}': profileB score ({scoreB}) clipped to {clippedScoreB} (range: {minScore}-{maxScore})."
            )

        balancedScore = (weightA * clippedScoreA) + (weightB * clippedScoreB)

        result['balancedProfile'][dim] = round(balancedScore, 3)

    return result
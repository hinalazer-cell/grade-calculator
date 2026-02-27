# grades.py
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80: 
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def class_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def highest_score(scores):
    best = scores[0]
    for score in scores:
        if score > best:
            best = score
    return best
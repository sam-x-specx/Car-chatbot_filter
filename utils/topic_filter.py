# Store the last valid car-related topic for context
last_topic = None

def is_on_topic(question, keywords=["car", "engine", "model", "price", "horsepower", "mileage", "vehicle", "build", "factory", "made", "where"]):
    global last_topic
    question = question.lower()

    # Check if the question explicitly contains a car-related keyword
    contains_keyword = any(keyword in question for keyword in keywords)

    if contains_keyword:
        # If the question is explicitly about cars, update the last topic
        last_topic = question
        return True
    elif last_topic:
        # If no keyword but there's a previous car-related topic, assume it's a follow-up
        # Allow short, vague questions like "where build" or "how fast" as follow-ups
        if len(question.split()) <= 3:  # Short questions are likely follow-ups
            return True
    
    return False

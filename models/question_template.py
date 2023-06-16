class Question_Template:
    def __init__(self, media, subject, question_id, description, difficulty, topic, subtopic, question_type, answer, csec_section, hint, status, name, question_text):
        self.media = media
        self.subject = subject
        self.question_id = question_id
        self.description = description
        self.difficulty = difficulty
        self.topic = topic
        self.subtopic = subtopic
        self.question_type = question_type
        self.answer = answer
        self.csec_section = csec_section
        self.hint = hint
        self.status = status
        self.name = name
        self.question_text = question_text

    def to_dict(self):
        return {
            "media": self.media,
            "subject": self.subject,
            "question_id": self.question_id,
            "description": self.description,
            "difficulty": self.difficulty,
            "topic": self.topic,
            "subtopic": self.subtopic,
            "question_type": self.question_type,
            "answer": self.answer,
            "csec_section": self.csec_section,
            "hint": self.hint,
            "status": self.status,
            "name": self.name,
            "question_text": self.question_text
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            media=data.get("media"),
            subject=data.get("subject"),
            question_id=data.get("question_id"),
            description=data.get("description"),
            difficulty=data.get("difficulty"),
            topic=data.get("topic"),
            subtopic=data.get("subtopic"),
            question_type=data.get("question_type"),
            answer=data.get("answer"),
            csec_section=data.get("csec_section"),
            hint=data.get("hint"),
            status=data.get("status"),
            name=data.get("name"),
            question_text=data.get("question_text")
        )

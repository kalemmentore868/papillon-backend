class Question_Template:
    def __init__(self, status, subject, name, description, cesc_section, objectives, format, text, type, difficulty, image, options, formula, hint, video, written_solution):
        self.status = status
        self.subject = subject
        self.name = name
        self.description = description
        self.csec_section = cesc_section
        self.objectives = objectives
        self.format = format
        self.text = text
        self.type = type
        self.difficulty = difficulty
        self.image = image
        self.options = options
        self.formula = formula
        self.hint = hint
        self.video = video
        self.written_solution = written_solution

    def to_dict(self):
        return {
            "status": self.status,
            "subject": self.subject,
            "name": self.name,
            "description": self.description,
            "cesc_section": self.csec_section,
            "objectives": self.objectives,
            "format": self.format,
            "text": self.text,
            "type": self.type,
            "difficulty": self.difficulty,
            "image": self.image,
            "options": self.options,
            "formula": self.formula,
            "hint": self.hint,
            "video": self.video,
            "written_solution": self.written_solution
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            status=data.get("status"),
            subject=data.get("subject"),
            name=data.get("name"),
            description=data.get("description"),
            cesc_section=data.get("csec_section"),
            objectives=data.get("objectives"),
            format=data.get("format"),
            text=data.get("text"),
            type=data.get("type"),
            difficulty=data.get("difficulty"),
            image=data.get("image"),
            options=data.get("options"),
            formula=data.get("formula"),
            hint=data.get("hint"),
            video=data.get("video"),
            written_solution=data.get("written_solution")
        )

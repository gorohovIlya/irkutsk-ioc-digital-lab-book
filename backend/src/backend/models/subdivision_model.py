from core.entity_model import EntityModel


class SubdivisionModel(EntityModel):

    @classmethod
    def create(cls, name: str):
        return cls(name=name)

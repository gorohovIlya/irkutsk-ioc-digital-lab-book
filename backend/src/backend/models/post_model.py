from core.entity_model import EntityModel


class PostModel(EntityModel):

    @classmethod
    def create(cls, name: str):
        return cls(name=name)

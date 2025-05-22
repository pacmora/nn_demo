from kink import inject

from src.model_generator.domain.model import Model


@inject
class ModelService:
    """Generates dict model with the provided ModelDTO information

    Args:
        model (ModelDTO): ModelDTO that contains all the attributes
        to get the dict from Model object

    Returns:
        Dict that represent the model.
    """

    def generate_model(self, model: Model):
        return model.model_to_dict()

import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from us_visa.exception import USvisaException
from us_visa.logger import logging


class TargetValueMapping:
    def __init__(self):
        self.Certified: int = 0
        self.Denied: int = 1

    def _asdict(self):
        return self.__dict__

    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))


class UsvisaModel:
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        """
        preprocessing_object : Input object of preprocessor
        trained_model_object : Input object of trained model
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, dataframe: DataFrame) -> DataFrame:
        """
        Function accepts raw inputs and then transform the raw inputs using preprocessing object
        which guarantees that the inputs are in the same format as the training data
        At last it performs prediction on transformed features.
        """
        logging.info("Entered predict method of UsvisaModel class")

        try:
            logging.info("Using trained model to get predictions")

            transformed_feature = self.preprocessing_object.transform(dataframe)

            logging.info("Used the trained model to get predictions")

            return self.trained_model_object.predict(transformed_feature)

        except Exception as e:
            raise USvisaException(e, sys)

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"

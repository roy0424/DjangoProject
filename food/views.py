from .models import Food, Brand, Category
from .serializer import FoodSerializer, BrandSerializer, CategorySerializer
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


food_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the food", title="name",),
        "energy": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the energy", title="energy",),
        "protein": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the protein", title="protein",),
        "fat": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the fat", title="fat",),
        "sugar": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the sugar", title="sugar",),
        "sodium": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the sodium", title="sodium",),
        "cholesterol": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the cholesterol", title="cholesterol",),
        "saturate_fat": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the saturate_fat", title="saturate_fat",),
        "trans_fat": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_fat", title="trans_fat",),
        'hydrate': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the hydrate", title="hydrate"),
        'saccharose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the saccharose", title="saccharose"),
        'glucose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the glucose", title="glucose"),
        'fructose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the fructose", title="fructose"),
        'lactose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the lactose", title="lactose"),
        'maltose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the maltose", title="maltose"),
        'dietary_fiber': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the dietary_fiber", title="dietary_fiber"),
        'calcium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the calcium", title="calcium"),
        'iron': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the iron", title="iron"),
        'magnesium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the magnesium", title="magnesium"),
        'phosphorus': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the phosphorus", title="phosphorus"),
        'kalium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the kalium", title="kalium"),
        'zinc': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the zinc", title="zinc"),
        'copper': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the copper", title="copper"),
        'manganese': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the manganese", title="manganese"),
        'selenium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the selenium", title="selenium"),
        'beta_carotene': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the beta_carotene", title="beta_carotene"),
        'vitamin_d3': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_d3", title="vitamin_d3"),
        'tocopherol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tocopherol", title="tocopherol"),
        'tocotrienols': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tocotrienols", title="tocotrienols"),
        'vitamin_b1': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b1", title="vitamin_b1"),
        'vitamin_b2': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b2", title="vitamin_b2"),
        'niacin': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the niacin", title="niacin"),
        'folate': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the folate", title="folate"),
        'vitamin_b12': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b12", title="vitamin_b12"),
        'vitamin_c': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_c", title="vitamin_c"),
        'amino_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the amino_acid", title="amino_acid"),
        'isoleucine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the isoleucine", title="isoleucine"),
        'leucine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the leucine", title="leucine"),
        'lysine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the lysine", title="lysine"),
        'methionine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the methionine", title="methionine"),
        'phenylalanine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the phenylalanine", title="phenylalanine"),
        'threonine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the threonine", title="threonine"),
        'valine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the valine", title="valine"),
        'histidine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the histidine", title="histidine"),
        'arginine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the arginine", title="arginine"),
        'tyrosine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tyrosine", title="tyrosine"),
        'cysteine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the cysteine", title="cysteine"),
        'alanine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the alanine", title="alanine"),
        'aspartic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the aspartic_acid", title="aspartic_acid"),
        'glutamic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the glutamic_acid", title="glutamic_acid"),
        'glycine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the glycine", title="glycine"),
        'proline': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the proline", title="proline"),
        'serine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the serine", title="serine"),
        'butyric_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the butyric_acid", title="butyric_acid"),
        'caproic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the caproic_acid", title="caproic_acid"),
        'caprylic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the caprylic_acid", title="caprylic_acid"),
        'capric_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the capric_acid", title="capric_acid"),
        'lauric_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the lauric_acid", title="lauric_acid"),
        'myristic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the myristic_acid", title="myristic_acid"),
        'palmitic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the palmitic_acid", title="palmitic_acid"),
        'stearic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the stearic_acid", title="stearic_acid"),
        'arachidic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the arachidic_acid", title="arachidic_acid"),
        'myristoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the myristoleic_acid", title="myristoleic_acid"),
        'palmitoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the palmitoleic_acid", title="palmitoleic_acid"),
        'oleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the oleic_acid", title="oleic_acid"),
        'vaccenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vaccenic_acid", title="vaccenic_acid"),
        'gadoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the gadoleic_acid", title="gadoleic_acid"),
        'linoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the linoleic_acid", title="linoleic_acid"),
        'alpha_linolenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the alpha_linolenic_acid", title="alpha_linolenic_acid"),
        'gamma_linolenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the gamma_linolenic_acid", title="gamma_linolenic_acid"),
        'eicosadienoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the eicosadienoic_acid", title="eicosadienoic_acid"),
        'arachidonic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the arachidonic_acid", title="arachidonic_acid"),
        'eicosatrienoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the eicosatrienoic_acid", title="eicosatrienoic_acid"),
        'eicosapentaenoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the eicosapentaenoic_acid", title="eicosapentaenoic_acid"),
        'docosapentaenoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the docosapentaenoic_acid", title="docosapentaenoic_acid"),
        'docosahexaenoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the docosahexaenoic_acid", title="docosahexaenoic_acid"),
        'trans_oleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_oleic_acid", title="trans_oleic_acid"),
        'trans_linoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_linoleic_acid", title="trans_linoleic_acid"),
        'trans_linolenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_linolenic_acid", title="trans_linolenic_acid"),
        'ash': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the ash", title="ash"),
        'caffeine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the caffeine", title="caffeine"),
        'retinol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the retinol", title="retinol"),
        'sugar_alcohol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the sugar_alcohol", title="sugar_alcohol"),
        'erythritol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the erythritol", title="erythritol"),
        'iodine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the iodine", title="iodine"),
        'chloride': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the chloride", title="chloride"),
        'vitamin_d': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_d", title="vitamin_d"),
        'vitamin_d1': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_d1", title="vitamin_d1"),
        'vitamin_e': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_e", title="vitamin_e"),
        'vitamin_k': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_k", title="vitamin_k"),
        'vitamin_k1': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_k1", title="vitamin_k1"),
        'vitamin_k2': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_k2", title="vitamin_k2"),
        'pantothenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the pantothenic_acid", title="pantothenic_acid"),
        'vitamin_b6': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b6", title="vitamin_b6"),
        'biotin': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the biotin", title="biotin"),
        'choline': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the choline", title="choline"),
        'tryptophan': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tryptophan", title="tryptophan"),
        'taurine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the taurine", title="taurine"),
        'omega_3_fatty_acids': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the omega_3_fatty_acids", title="omega_3_fatty_acids"),
        'total_unsaturated_fats': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the total_unsaturated_fats", title="total_unsaturated_fats"),
        "brand": openapi.Schema(type=openapi.TYPE_INTEGER, description="Foreign key of the brand", title="brand"),
        "category": openapi.Schema(type=openapi.TYPE_INTEGER, description="Foreign key of the category", title="category"),
    },
    required=['name'],
)


result_food_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING, description="Id of the food", title="id",),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the food", title="name",),
        "energy": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the energy", title="energy",),
        "protein": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the protein", title="protein",),
        "fat": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the fat", title="fat",),
        "sugar": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the sugar", title="sugar",),
        "sodium": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the sodium", title="sodium",),
        "cholesterol": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the cholesterol", title="cholesterol",),
        "saturate_fat": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the saturate_fat", title="saturate_fat",),
        "trans_fat": openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_fat", title="trans_fat",),
        'hydrate': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the hydrate", title="hydrate"),
        'saccharose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the saccharose", title="saccharose"),
        'glucose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the glucose", title="glucose"),
        'fructose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the fructose", title="fructose"),
        'lactose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the lactose", title="lactose"),
        'maltose': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the maltose", title="maltose"),
        'dietary_fiber': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the dietary_fiber", title="dietary_fiber"),
        'calcium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the calcium", title="calcium"),
        'iron': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the iron", title="iron"),
        'magnesium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the magnesium", title="magnesium"),
        'phosphorus': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the phosphorus", title="phosphorus"),
        'kalium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the kalium", title="kalium"),
        'zinc': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the zinc", title="zinc"),
        'copper': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the copper", title="copper"),
        'manganese': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the manganese", title="manganese"),
        'selenium': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the selenium", title="selenium"),
        'beta_carotene': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the beta_carotene", title="beta_carotene"),
        'vitamin_d3': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_d3", title="vitamin_d3"),
        'tocopherol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tocopherol", title="tocopherol"),
        'tocotrienols': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tocotrienols", title="tocotrienols"),
        'vitamin_b1': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b1", title="vitamin_b1"),
        'vitamin_b2': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b2", title="vitamin_b2"),
        'niacin': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the niacin", title="niacin"),
        'folate': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the folate", title="folate"),
        'vitamin_b12': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b12", title="vitamin_b12"),
        'vitamin_c': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_c", title="vitamin_c"),
        'amino_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the amino_acid", title="amino_acid"),
        'isoleucine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the isoleucine", title="isoleucine"),
        'leucine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the leucine", title="leucine"),
        'lysine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the lysine", title="lysine"),
        'methionine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the methionine", title="methionine"),
        'phenylalanine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the phenylalanine", title="phenylalanine"),
        'threonine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the threonine", title="threonine"),
        'valine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the valine", title="valine"),
        'histidine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the histidine", title="histidine"),
        'arginine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the arginine", title="arginine"),
        'tyrosine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tyrosine", title="tyrosine"),
        'cysteine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the cysteine", title="cysteine"),
        'alanine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the alanine", title="alanine"),
        'aspartic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the aspartic_acid", title="aspartic_acid"),
        'glutamic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the glutamic_acid", title="glutamic_acid"),
        'glycine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the glycine", title="glycine"),
        'proline': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the proline", title="proline"),
        'serine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the serine", title="serine"),
        'butyric_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the butyric_acid", title="butyric_acid"),
        'caproic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the caproic_acid", title="caproic_acid"),
        'caprylic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the caprylic_acid", title="caprylic_acid"),
        'capric_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the capric_acid", title="capric_acid"),
        'lauric_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the lauric_acid", title="lauric_acid"),
        'myristic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the myristic_acid", title="myristic_acid"),
        'palmitic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the palmitic_acid", title="palmitic_acid"),
        'stearic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the stearic_acid", title="stearic_acid"),
        'arachidic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the arachidic_acid", title="arachidic_acid"),
        'myristoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the myristoleic_acid", title="myristoleic_acid"),
        'palmitoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the palmitoleic_acid", title="palmitoleic_acid"),
        'oleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the oleic_acid", title="oleic_acid"),
        'vaccenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vaccenic_acid", title="vaccenic_acid"),
        'gadoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the gadoleic_acid", title="gadoleic_acid"),
        'linoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the linoleic_acid", title="linoleic_acid"),
        'alpha_linolenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the alpha_linolenic_acid", title="alpha_linolenic_acid"),
        'gamma_linolenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the gamma_linolenic_acid", title="gamma_linolenic_acid"),
        'eicosadienoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the eicosadienoic_acid", title="eicosadienoic_acid"),
        'arachidonic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the arachidonic_acid", title="arachidonic_acid"),
        'eicosatrienoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the eicosatrienoic_acid", title="eicosatrienoic_acid"),
        'eicosapentaenoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the eicosapentaenoic_acid", title="eicosapentaenoic_acid"),
        'docosapentaenoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the docosapentaenoic_acid", title="docosapentaenoic_acid"),
        'docosahexaenoic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the docosahexaenoic_acid", title="docosahexaenoic_acid"),
        'trans_oleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_oleic_acid", title="trans_oleic_acid"),
        'trans_linoleic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_linoleic_acid", title="trans_linoleic_acid"),
        'trans_linolenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the trans_linolenic_acid", title="trans_linolenic_acid"),
        'ash': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the ash", title="ash"),
        'caffeine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the caffeine", title="caffeine"),
        'retinol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the retinol", title="retinol"),
        'sugar_alcohol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the sugar_alcohol", title="sugar_alcohol"),
        'erythritol': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the erythritol", title="erythritol"),
        'iodine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the iodine", title="iodine"),
        'chloride': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the chloride", title="chloride"),
        'vitamin_d': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_d", title="vitamin_d"),
        'vitamin_d1': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_d1", title="vitamin_d1"),
        'vitamin_e': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_e", title="vitamin_e"),
        'vitamin_k': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_k", title="vitamin_k"),
        'vitamin_k1': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_k1", title="vitamin_k1"),
        'vitamin_k2': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_k2", title="vitamin_k2"),
        'pantothenic_acid': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the pantothenic_acid", title="pantothenic_acid"),
        'vitamin_b6': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the vitamin_b6", title="vitamin_b6"),
        'biotin': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the biotin", title="biotin"),
        'choline': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the choline", title="choline"),
        'tryptophan': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the tryptophan", title="tryptophan"),
        'taurine': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the taurine", title="taurine"),
        'omega_3_fatty_acids': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the omega_3_fatty_acids", title="omega_3_fatty_acids"),
        'total_unsaturated_fats': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_FLOAT, description="Value of the total_unsaturated_fats", title="total_unsaturated_fats"),
        "brand": openapi.Schema(type=openapi.TYPE_INTEGER, description="Foreign key of the brand", title="brand"),
        "category": openapi.Schema(type=openapi.TYPE_INTEGER, description="Foreign key of the category", title="category"),
    },
    required=['name'],
)


page_param = openapi.Parameter(
    'page',
    openapi.IN_QUERY,
    description="Page number",
    type=openapi.TYPE_INTEGER,
    example=2,
    default=1,
)

size_param = openapi.Parameter(
    'size',
    openapi.IN_QUERY,
    description="Number of items per page",
    type=openapi.TYPE_INTEGER,
    example=10,
    default=10,
)


auth_token_param = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description="Bearer authentication token",
    type=openapi.TYPE_STRING,
    example="Bearer YOUR_SAMPLE_TOKEN_HERE",
    required=["Authorization"],
)


@swagger_auto_schema(method='POST', tags=["food"], manual_parameters=[auth_token_param], request_body=food_schema, operation_description="Insert a food with nutrients", responses={201:result_food_schema, 400:'BAD REQUEST',},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def create_food(request):
    if request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


one_food_param = openapi.Parameter(
    name="food_id",
    in_=openapi.IN_PATH,
    description="ID of the food",
    required=True,
    type=openapi.TYPE_INTEGER,
)


@swagger_auto_schema(method='GET', tags=["food"], manual_parameters=[one_food_param], operation_description="Get ONE food", responses={200:result_food_schema, 404:"Not Found"},)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    serializer = FoodSerializer(food)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', tags=["food"], manual_parameters=[page_param, size_param], operation_description="Get ALL food", responses={200:result_food_schema},)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_food(request):
    foods = Food.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10  # 또는 settings.py에서 설정한 PAGE_SIZE를 사용
    paginated_foods = paginator.paginate_queryset(foods, request)
    serializer = FoodSerializer(paginated_foods, many=True)
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(method='POST', tags=["food"], manual_parameters=[auth_token_param, one_food_param], request_body=food_schema, operation_description="Update ONE food\nChange attribute's value", responses={200:result_food_schema, 400:"Bad Request", 404:"Not Found"},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def update_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', tags=["food"], manual_parameters=[auth_token_param, one_food_param], operation_description="Delete ONE food", responses={204:"No Content", 404:"Not Found",},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


token_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "token": openapi.Schema(type=openapi.TYPE_STRING, description="Your access token", title="token")
    },
    required=["token"],
)


@swagger_auto_schema(method='POST', tags=["api"], manual_parameters=[auth_token_param], request_body=token_schema, operation_description="To verify your token", responses={200:token_schema, 400:"Bad Request" , 401:"Unauthorized",},)
@api_view(['POST'])
def verify_token(request):
    token = request.data.get('token')

    if not token:
        return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        UntypedToken(token)
    except (InvalidToken, TokenError) as e:
        return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'status': 'Token is valid'}, status=status.HTTP_200_OK)


brand_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of brand", title="name"),
    },
    required=["name",],
)


result_brand_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING, description="id of brand", title="id"),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of brand", title="name"),
    },
    required=["name",],
)


@swagger_auto_schema(method='POST', tags=["brand"],manual_parameters=[auth_token_param], request_body=brand_schema, operation_description="Insert a brand", responses={201:result_brand_schema, 400:'BAD REQUEST',},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def create_brand(request):
    if request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


one_brand_param = openapi.Parameter(
    name="brand_id",
    in_=openapi.IN_PATH,
    description="ID of the brand",
    required=True,
    type=openapi.TYPE_INTEGER,
)


@swagger_auto_schema(method='GET', tags=["brand"], manual_parameters=[one_brand_param], operation_description="Get ONE brand", responses={200:result_brand_schema, 404:"Not Found"},)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_brand(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    serializer = BrandSerializer(brand)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', tags=["brand"], manual_parameters=[page_param, size_param], operation_description="Get ALL brand", responses={200:result_brand_schema},)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_brand(request):
    brands = Brand.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10  # 또는 settings.py에서 설정한 PAGE_SIZE를 사용
    paginated_brands = paginator.paginate_queryset(brands, request)
    serializer = BrandSerializer(paginated_brands, many=True)
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(method='POST', tags=["brand"], manual_parameters=[auth_token_param, one_brand_param], request_body=brand_schema, operation_description="Update ONE brand\nChange attribute's value", responses={200:result_brand_schema, 400:"Bad Request", 404:"Not Found"},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    if request.method == 'POST':
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', tags=["brand"], manual_parameters=[auth_token_param, one_brand_param], operation_description="Delete ONE brand", responses={204:"No Content", 404:"Not Found",},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    brand.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


category_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of category", title="name"),
    },
    required=["name",],
)


result_category_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_STRING, description="id of category", title="id"),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of category", title="name"),
    },
    required=["name",],
)


@swagger_auto_schema(method='POST', tags=["category"], manual_parameters=[auth_token_param], request_body=category_schema, operation_description="Insert a category", responses={201:result_category_schema, 400:'BAD REQUEST',},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def create_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


one_category_param = openapi.Parameter(
    name="category_id",
    in_=openapi.IN_PATH,
    description="ID of the category",
    required=True,
    type=openapi.TYPE_INTEGER,
)


@swagger_auto_schema(method='GET', tags=["category"], manual_parameters=[one_category_param], operation_description="Get ONE category", responses={200:result_category_schema, 404:"Not Found"},)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', tags=["category"], manual_parameters=[page_param, size_param], operation_description="Get ALL category", responses={200:result_category_schema},)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_all_category(request):
    categories = Category.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10  # 또는 settings.py에서 설정한 PAGE_SIZE를 사용
    paginated_categories = paginator.paginate_queryset(categories, request)
    serializer = CategorySerializer(paginated_categories, many=True)
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(method='POST', tags=["category"], manual_parameters=[auth_token_param, one_category_param], request_body=category_schema, operation_description="Update ONE category\nChange attribute's value", responses={200:result_category_schema, 400:"Bad Request", 404:"Not Found"},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', tags=["category"], manual_parameters=[auth_token_param, one_category_param], operation_description="Delete ONE category", responses={204:"No Content", 404:"Not Found",},)
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep # Utile pour l'attente lors du débogage

BASE_URL = os.environ.get("APP_URL", "http://localhost:5000")

@pytest.fixture(scope="module")
def driver():
    """Initialise et configure le navigateur Chrome pour les tests."""
    options = webdriver.ChromeOptions()
    # Options nécessaires pour que Chrome fonctionne sans interface graphique dans l'environnement CI/CD
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Installation et démarrage du service Chrome
    service = ChromeService(ChromeDriverManager().install())
    
    # Création de l'instance du navigateur
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10) # Attendre 10 secondes implicitement pour les éléments
    yield driver
    
    # Fermeture du navigateur après les tests
    driver.quit()

def test_homepage_title_and_water_form(driver):
    """Teste si la page d'accueil se charge et contient les éléments clés."""
    print(f"Testing URL: {BASE_URL}")
    driver.get(BASE_URL)
    
    # 1. Vérification du titre de la page
    assert "Water Tracker" in driver.title, "Le titre de la page doit contenir 'Water Tracker'"
    
    # 2. Vérification de la présence d'un titre principal (ex: H1)
    main_heading = driver.find_element(By.TAG_NAME, "h1")
    assert "Bienvenue" in main_heading.text or "Tracker" in main_heading.text, "Le titre principal est introuvable."
    
    # 3. Vérification de la présence du formulaire d'entrée de l'eau (exemple basé sur des hypothèses)
    try:
        water_input = driver.find_element(By.ID, "water_input") # Supposons que l'ID est 'water_input'
    except:
        water_input = driver.find_element(By.NAME, "water") # Ou supposons que le nom est 'water'
    
    assert water_input.is_displayed(), "Le champ de saisie de l'eau doit être visible."

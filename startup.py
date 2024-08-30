import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))) #recuperer l'endroi de travail
temp = sys.path #temporaire permettant de revenir a la racine
sys.path = sys.path + ["test"] #ajouter ou l'on veur aller
import test.demo as demo    #activer le premier plugin
sys.path = temp #reset
import miaou as miaou #import de second plugin







# QgsProject.instance().legendLayersAdded.connect(wawa)



# from qgis.core import QgsMapLayer
# from qgis.core import QgsProject
# from qgis.utils import iface
# import sys
# sys.path = [""] + sys.path
# import PluginBuilder    #Activation sub

# QgsProject.instance().legendLayersAdded.connect(PluginBuilder)




# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# import demo
import PriaidDiagnosisClient
import config
import sys
import json

import tkinter as tk




class PriaidDiagnosisClientDemo:
    'Demo class to simulate how to use PriaidDiagnosisClient'

    def __init__(self):
        username = config.username
        password = config.password
        authUrl = config.priaid_authservice_url
        healthUrl = config.priaid_healthservice_url
        language = config.language
        self._printRawOutput = config.pritnRawOutput
        self.window = tk.Tk()

        self._diagnosisClient = PriaidDiagnosisClient.DiagnosisClient(username, password, authUrl, language, healthUrl)

    def simulate(self):
        # Load body locations
        selectedLocationID = self._loadBodyLocations()

        self.window.mainloop() 


    def _loadBodyLocations(self):   # takes list of body locations from API
        bodyLocations = self._diagnosisClient.loadBodyLocations()
        
        if not bodyLocations:
            raise Exception("Empty body locations results")
         
        for bodyLocation in bodyLocations:
            print("{0} ({1})".format(bodyLocation["Name"], bodyLocation["ID"]))

        
        selectedLocation = bodyLocations[0]  ## change to user input
        print("Sublocations for selected location {0}".format(selectedLocation["Name"]))

        tkSelectedLocation = tk.StringVar()
        tkSelectedLocation.set(selectedLocation) 
       
        label = tk.Label(self.window, textvariable = tkSelectedLocation)
        label.pack()

        return selectedLocation["ID"]

diagnosisClientDemo = PriaidDiagnosisClientDemo()
diagnosisClientDemo.simulate()


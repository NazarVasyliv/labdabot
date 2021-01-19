import pandas as pd


def wavelength(file_to_wl_name, chat_id):
    df = pd.read_csv((file_to_wl_name), sep='\t', skiprows=10)
    df = df.loc[:, df.columns.intersection(['CID','Label'])]
    wl = []
    wlp = []

    for row in df.itertuples(index=True, name='Pandas'):
      RowStringCID= getattr(row, "CID")
      RowStringLabel = getattr(row, "Label")
      if RowStringLabel.find("RETN") == -1:
        if RowStringCID.find("-P") == -1:
          if RowStringLabel.find("-P") == -1 and RowStringCID.find("WLP") == -1 and RowStringCID.find("!!!") == -1 and RowStringLabel.find("!!!") == -1:
            wl.append(RowStringCID)
          elif RowStringCID.find("WLP") >= 0 or RowStringCID.find("!!!") >= 0 or RowStringLabel.find("!!!") >= 0 or RowStringLabel.find('FI'):
            wlp.append(RowStringCID)

        elif RowStringCID.find("-P") > 0:
          if (RowStringCID.find("WLP") >= 0 or RowStringCID.find("!!!") >= 0 or RowStringLabel.find("!!!") >= 0):
            RowStringCID = RowStringCID.replace("-P", "")
            wlp.append(RowStringCID)

    wlframe = pd.DataFrame({'WL' : wl})
    wlpframe = pd.DataFrame({'WLP' : wlp})
    retn = pd.concat([wlframe, wlpframe], axis=1)
    path_to_excel = '/content/lambda_issue' + chat_id
    export_excel = retn.to_excel (path_to_excel, index = None, header=True)
    return path_to_excel

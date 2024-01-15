import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


def parse(CREDENTIALS_FILE, spreadsheet_id) -> list[list[str]]:
    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # Пример чтения файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:M11',
        majorDimension='COLUMNS').execute()

    return values['values']

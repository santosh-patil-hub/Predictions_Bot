import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import CREDENTIALS_PATH, GOOGLE_SHEET_NAME

def get_worksheet(title="Trade Log"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)
    client = gspread.authorize(creds)
    sheet = client.open(GOOGLE_SHEET_NAME)
    try:
        return sheet.worksheet(title)
    except:
        return sheet.add_worksheet(title, rows=1000, cols=10)




def log_signals_to_sheet(df, stock):
    sheet = get_worksheet(stock)
    sheet.clear()
    df.reset_index(inplace=True)
    df = df[['Date', 'Close', 'RSI', '20DMA', '50DMA', 'Signal']]
    df = df.dropna().copy()
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df.columns = [str(col) if col != '' else 'Unnamed' for col in df.columns]
    df = df.astype(str)
    sheet.update([df.columns.tolist()] + df.values.tolist())

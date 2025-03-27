import datetime as DT

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

def PhoneNumDsp(PhoneNum):
    #Function that will concatenate a phone number to the format (###) ###-####
    
    PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
    
    return PhoneNum

def GetPayDue(InvoiceDate):
    # Determine the payment date based on 20 days after the invoice date
    # or the first day of the next month - whichever is later.

    Pay20Date = InvoiceDate + DT.timedelta(days=20)
    PurYear = InvoiceDate.year
    PurMonth = InvoiceDate.month
    PurDay = InvoiceDate.day

    PayYear = PurYear
    PayMonth = PurMonth + 1
    if PayMonth == 13:
        PayMonth -= 12
        PayYear += 1
    PayDay = 1
    PayFirstDate = DT.datetime(PayYear, PayMonth, PayDay)

    if Pay20Date > PayFirstDate:
        PayDate = Pay20Date
    else:
        PayDate = PayFirstDate

    return PayDate

def GetInsCosts(NumCars, ExtraLia, GlassCov, LoanCar, DownPay, BASIC_PRE_FEE, ADD_CAR_DIS, EX_LIA_FEE, GLASS_FEE, LOAN_CAR_FEE, HST_RATE):
    # Calculate the costs neccesary for the Insurance Invoice and return the calculations.
    #(Insurance Premium, Extra Liability Cost, Glass Coverage Cost, Loaner Car Cost, Total Extra Costs, Total Insurance Premium, HST, Total Cost & Monthly Payments)
    if NumCars == 1:
        InsPre = BASIC_PRE_FEE
    else:
        InsPre = BASIC_PRE_FEE + (NumCars - 1) * BASIC_PRE_FEE * ADD_CAR_DIS
        
    if ExtraLia == "Y":
        LiaCost = EX_LIA_FEE
    else:
        LiaCost = 0
    
    if GlassCov == "Y":
        GlassCost = GLASS_FEE
    else:
        GlassCost = 0
        
    if LoanCar == "Y":
        LoanCost = LOAN_CAR_FEE
    else:
        LoanCost = 0
        
    TotExtraCost = LiaCost + GlassCost + LoanCost
    TotInsPre = InsPre + TotExtraCost
    HST = TotInsPre * HST_RATE
    TotCost = TotInsPre + HST
    
    if DownPay == 0:
        MonPay = (TotCost + 39.99) / 8
    else:
        MonPay = (TotCost - DownPay + 39.99) / 8
    
    return InsPre, LiaCost, GlassCost, LoanCost, TotExtraCost, TotInsPre, HST, TotCost, MonPay
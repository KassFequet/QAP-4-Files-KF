# Description: QAP 4 - Car Insurance Policy
# Author: Kassaundra Fequet
# Date(s): March 14/25 - Mar 27/25


# Define required libraries.
import FormatValues as FV
import datetime as DT


# Define program constants.
POL_NO = 1944
BASIC_PRE_FEE = 869.00
ADD_CAR_DIS = .25

EX_LIA_FEE = 130.00
GLASS_FEE = 86.00
LOAN_CAR_FEE = 58.00

HST_RATE = .15
MON_PROC_FEE = 39.99
CUR_DATE = DT.datetime.now()

PROV_TERR_LIST = [ "NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU" ]
PAY_METH_LIST = [ "Full", "Monthly", "Down Pay" ]


ClaimNumLst = ["12345", "67890"]  # Example claim numbers
ClaimDateLst = [DT.date(2025, 3, 15), DT.date(2025, 3, 20)]  # Example claim dates
ClaimAmtLst = [1500.00, 2500.00]  # Example claim amounts



# Define program functions.
# See imported library FormatValues

# Main program starts here.
Customer = True

while True:
    
    AllowedUpperCharNum = set("ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789")

    while True:
        print()
        FName = input("Enter the customer's first name:                                                    ").title()
        if FName == "":
            print()
            print("   Data Entry Error - First name cannot be blank.")
            print()
        else:
            break

    while True:
        LName = input("Enter the customer's last name:                                                     ").title()
        if LName == "":
            print()
            print("   Data Entry Error - Last name cannot be blank.")
            print()
        else:
            break

    while True:
        StAdd = input("Enter the customer's street address:                                                ").title()
        if StAdd == "":
            print()
            print("   Data Entry Error - Street address cannot be blank.")
            print()
        else:
            break

    while True:
        City = input("Enter the customer's city:                                                          ").title()
        if City == "":
            print()
            print("   Data Entry Error - City cannot be blank.")
            print()
        else:
            break

    while True:
        ProvTerr = input("Enter the customer's province/territory (XX):                                       ").upper()
        if ProvTerr == "":
            print()
            print("   Data Entry Error - Province/Territory cannot be blank.")
            print()
        elif len(ProvTerr) != 2:
            print()
            print("   Data Entry Error - Province/Territory must contain only 2 characters")
            print()
        elif ProvTerr not in PROV_TERR_LIST:
            print()
            print("   Data Entry Error - Invalid Province/Territory")
            print()
        else:
            break

    while True:
        PostCode = input("Enter the customer's postal code (X#X#X#):                                          ").upper()
        if PostCode == "":
            print()
            print("    Data Entry Error - Customer postal code must be entered.")
            print()
        elif len(PostCode) != 6:
            print()
            print("    Data Entry Error - Postal code  must contain 6 characters only.")
            print()
        elif set(PostCode).issubset(AllowedUpperCharNum) == False:
            print()
            print("    Data Entry Error - Customer postal code contains invalid characters.")
            print()
        else:
            break

    while True:
        PhoneNum = input("Enter the customer's phone number (##########):                                     ")
        if PhoneNum == "":
            print()
            print("   Data Entry Error - Phone number cannot be blank")
            print()
        elif len(PhoneNum) != 10:
            print()
            print("   Data Entry Error - Phone number must contain 10 digits only")
            print()
        elif PhoneNum.isdigit() == False:
            print()
            print("   Data Entry Error - Phone number contains invalid characters")
            print()
        else:
            break

    while True:
        NumCars = input("Enter the number of cars being insured:                                             ")
        try:
            NumCars = int(NumCars)
            break
        except ValueError:
            print()
            print("   Data Entry Error - Please enter a valid number.")
            print()

    while True:
        ExtraLia = input("Would the customer like extra liability up to $1,000,000 (Y/N):                     ").upper()
        if ExtraLia == "":
            print()
            print("   Data Entry Error - Extra liability cannot be blank.")
            print()
        elif ExtraLia != "Y" and ExtraLia != "N":
            print()
            print("   Data Entry Error - Input Y for Yes or N for No")
            print()
        else:
            break

    while True:
        GlassCov = input("Would the customer like optional glass coverage (Y/N):                              ").upper()
        if GlassCov == "":
            print()
            print("   Data Entry Error - Glass coverage cannot be blank.")
            print()
        elif GlassCov != "Y" and GlassCov != "N":
            print()
            print("   Data Entry Error - Input Y for Yes or N for No")
            print()
        else:
            break

    while True:
        LoanCar = input("Would the customer like an optional loaner car (Y/N):                               ").upper()
        if LoanCar == "":
            print()
            print("   Data Entry Error - Loaner car coverage cannot be blank.")
            print()
        elif LoanCar != "Y" and LoanCar != "N":
            print()
            print("   Data Entry Error - Input Y for Yes or N for No")
            print()
        else:
            break

    DownPay = 0
    while True:
        PayMeth = input("What method of payment would the customer like to make (Full, Monthly or Down Pay): ").title()
        if PayMeth == "":
            print()
            print("   Data Entry Error - Payment method cannot be blank.")
            print()
        elif PayMeth not in PAY_METH_LIST:
            print()
            print("   Data Entry Error - Invalid Payment Method")
            print()
        elif PayMeth == "Down Pay":
            DownPay = input("Enter the amount of the down payment:                                               ")
            try:
                DownPay = float(DownPay)
                break
            except ValueError:
                print()
                print("   Data Entry Error - Please enter a valid amount.")
                print()
        else:
            break

    # Claim detail questions will repeat if user answers yes
    while True:
        ClaimNum = input("Enter the claim number (#####):                                                     ").title()
        if ClaimNum.isdigit() and len(ClaimNum) == 5:
            ClaimNumLst.append(ClaimNum)
            break
        else:
            print()
            print("   Data Entry Error - Please enter a 5 digit number.")
            print()

    while True:
        ClaimDate = input("Enter the claim date (YYYY-MM-DD):                                                  ")
        try:
            ClaimDate = DT.datetime.strptime(ClaimDate, "%Y-%m-%d").date()
            ClaimDateLst.append(ClaimDate)
            break
        except ValueError:
            print()
            print("   Data Entry Error - Please enter the date as YYYY-MM-DD.")
            print()

    while True:
        ClaimAmt = input("Enter the claim amount:                                                             ")
        if ClaimAmt.isdigit():
            ClaimAmt = float(ClaimAmt)
            ClaimAmtLst.append(ClaimAmt)
            break
        else:
            print()
            print("   Data Entry Error - Please enter a valid number.")
            print()

    # Perform required calculations for the customer information. Not needed if processing another claim for the customer.

    InsPre, LiaCost, GlassCost, LoanCost, TotExtraCost, TotInsPre, HST, TotCost, MonPay = FV.GetInsCosts(
        NumCars, ExtraLia, GlassCov, LoanCar, DownPay, BASIC_PRE_FEE, ADD_CAR_DIS, EX_LIA_FEE, GLASS_FEE, LOAN_CAR_FEE, HST_RATE
    )
    PayDueDate = FV.GetPayDue(CUR_DATE)
    CustNameDsp = FName + " " + LName
    TopAddressDsp = StAdd + ", " + City
    BottomAddressDsp = ProvTerr + " " + PostCode
    PhoneNum = FV.PhoneNumDsp(PhoneNum)

    # Display results
    print()
    print(f"                    ONE STOP INSURANCE COMPANY")
    print(f"                         CUSTOMER INVOICE")
    print()
    print(f"                                            Policy Number:        {POL_NO:>4d}")
    print(f" Customer Information:                      Invoice Date:   {FV.FDateS(CUR_DATE)}")
    print(f"     {CustNameDsp:<25s}              Number of Cars Insured: {NumCars:>2d}")
    print(f"     {TopAddressDsp:<25s}            ----------------------------")
    print(f"     {BottomAddressDsp:<10s}                                OPTIONAL COVERAGES")
    print(f"     {PhoneNum:<14s}                        Extra Liability: {FV.FDollar2(LiaCost):>10s}")
    print(f"                                           Glass Coverage:  {FV.FDollar2(GlassCost):>10s}")
    print(f"                                           Loaner Car:      {FV.FDollar2(GlassCost):>10s}")
    print(f"-----------------------------------------------------------------------")

    if PayMeth == "Down Pay":
        print(f" Down Payment:   {FV.FDollar2(DownPay):>10s}               Insurance Premium:{FV.FDollar2(InsPre):>10s}")
    else:
        print(f"                                          Insurance Premium:{FV.FDollar2(InsPre):>10s}")

    if PayMeth == "Down Pay" or PayMeth == "Monthly":
        print(f"                                          Total Extra:      {FV.FDollar2(TotExtraCost):>10s}")
        print(f" Payment Method:    Monthly               HST:              {FV.FDollar2(HST):>10s}")
        print(f" Monthly Amount: {FV.FDollar2(MonPay):>10s}               Total:            {FV.FDollar2(TotCost):>10s}")
    else:
        print(f"                                          Total Extra:      {FV.FDollar2(TotExtraCost):>10s}")
        print(f"                                          HST:              {FV.FDollar2(HST):>10s}")
        print(f"  Payment Method: Full                    Total:            {FV.FDollar2(TotCost):>10s}")

    print(f"-----------------------------------------------------------------------")
    print(f"     Claim #                 Claim Date                 Amount")
    print(f"-----------------------------------------------------------------------")

    # Loop through the lists and print each claim's details
    for i in range(len(ClaimNumLst)):
        print(f"      {ClaimNumLst[i]:<10s}             {FV.FDateS(ClaimDateLst[i]):<15s}         {FV.FDollar2(ClaimAmtLst[i]):>10s}")

    print(f"-----------------------------------------------------------------------")


    # Write the values to a data file for storage.
    f = open("Policies.dat", "a")
    
    f.write(f"{FName}, ")
    f.write(f"{LName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{ProvTerr}, ")
    f.write(f"{PostCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{ExtraLia}, ")
    f.write(f"{GlassCov}, ")
    f.write(f"{LoanCar}, ")
    f.write(f"{PayMeth}, ")
    f.write(f"{DownPay}, ")
    f.write(f"{ClaimNum}, ")
    f.write(f"{ClaimDate}, ")
    f.write(f"{ClaimAmt}, ")
    f.write(f"{TotCost},\n ")

    f.close()

    # Ask if the user wants to process another claim
    
    Continue = input("Do you want to process another claim (Y/N): ").upper()
    
    if Continue == "N":
        print()
        print("               Thank you for using One Stop Insurance!")
        print()
        break
    
# Any housekeeping duties at the end of the program.
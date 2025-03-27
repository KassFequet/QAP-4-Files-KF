// Desc: QAP 4 - St. John's Marina & Yacht Club - Yearly Member Receipt //
//Author: Kassaundra Fequet
//Dates: Mar 17/25 - Mar 27/25

//Define program constants //
const EVEN_SITE_RATE = 80.0; //Even numbered sites cost $80/month.//
const ODD_SITE_RATE = 120.0; //Odd numbered sites cost $120/month.//
const ALT_MEM_RATE = 5.0; //Each alternate member costs $5/month.//

const CLEAN_RATE = 50.0; //Weekly site cleaning costs $50/month.//
const VIDEO_RATE = 35.0; //Video surveillance costs $35/month.//

const HST_RATE = 0.15; //The current HST rate is 15%.//

const STAN_MONTH_RATE = 75.0; //Standard members have a monthly dues rate of $75/month.//
const EXEC_MONTH_RATE = 150.0; //Executive members have a monthly dues rate of $150/month.//

const PROC_RATE = 59.99; //The processing fee is $59.99.//
const CAN_RATE = 0.6; //The cancellation fee is 60% of the yearly site charges.//

//Define format options for printing//
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const num0Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "0",
  maximumFractionDigits: "0",
});

//Gather user input.

let Date = prompt("Enter the current date(YYYY-MM-DD): ");
let SiteNum = prompt("Enter the site number (1-100): ");
SiteNum = parseInt(SiteNum);

let MemName = prompt("Enter the members name: ");
let StAdd = prompt("Enter the street address: ");
let City = prompt("Enter the city: ");
let Prov = prompt("Enter the province (XX): ").toUpperCase();
let PostCode = prompt("Enter the postal code (X#X #X#): ").toUpperCase();

let HomePhone = prompt("Enter the home phone number (##########): ");
let CellPhone = prompt("Enter the cell phone number (##########): ");

let MemType = prompt("Enter the membership type (S/E): ").toUpperCase();
let NumAltMem = prompt("Enter the number of alternate members: "); //Family and friends that are allowed to access the grounds.//
NumAltMem = parseInt(NumAltMem);

let Clean = prompt("Do you want weekly site cleaning? (Y/N): ").toUpperCase();
let Video = prompt("Do you want video surveillance? (Y/N): ").toUpperCase();

// Perform program calculations and generate results.

let NumSiteCharge = ODD_SITE_RATE;
if (SiteNum / 2 == 0) {
  NumSiteCharge = EVEN_SITE_RATE;
}

let AltMemCharge = NumAltMem * ALT_MEM_RATE;
let SiteCharge = NumSiteCharge + AltMemCharge;

let CleanCharge = 0;
let CleanAns = "No";
if (Clean == "Y") {
  CleanCharge = CLEAN_RATE;
  CleanAns = "Yes";
}

let VideoCharge = 0;
let VideoAns = "No";
if (Video == "Y") {
  VideoCharge = VIDEO_RATE;
  VideoAns = "Yes";
}

let ExtraCharge = CleanCharge + VideoCharge;

let Subtotal = SiteCharge + ExtraCharge;
let HST = Subtotal * HST_RATE;
let TotMonCharge = Subtotal + HST;

let MonDues = STAN_MONTH_RATE;
let MemTypeAns = "Standard";
if (MemType == "E") {
  MonDues = EXEC_MONTH_RATE;
  MemTypeAns = "Executive";
}

let TotMonFee = TotMonCharge + MonDues;

//In the 3 following calculations, 12 represents the amount of months per year//
let TotYearFee = TotMonFee * 12;
let MonPay = (TotYearFee + PROC_RATE) / 12;
let CanFee = SiteCharge * 12 * CAN_RATE;

// Prepare the receipt for the customer in a table.

document.writeln("<br />");
document.writeln("<table class='receipttable'>");

document.writeln("<tr class='centertext'>");
document.writeln(
  "<td>St. John's Marina & Yacht Club<br />Yearly Member Receipt<br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br />Client Name and Address:<br /><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td>" +
    MemName +
    "<br />" +
    StAdd +
    "<br />" +
    City +
    ", " +
    Prov +
    " " +
    PostCode +
    "<br />"
);
document.writeln("<br />");
document.writeln("Phone: " + HomePhone + " (H)");
document.writeln(
  "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + CellPhone + " (C)</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Site #: " +
    SiteNum +
    "</span>" +
    "<span class='righttext'>Member type: " +
    MemTypeAns +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Alternate members:" +
    "</span>" +
    "<span class='righttext'>" +
    num0Format.format(NumAltMem) +
    "</span><br />"
);
document.writeln(
  "<span class='lefttext'>Weekly site cleaning:" +
    "</span>" +
    "<span class='righttext'>" +
    CleanAns +
    "</span><br />"
);
document.writeln(
  "<span class='lefttext'>Video surveillance:" +
    "</span>" +
    "<span class='righttext'>" +
    VideoAns +
    "</span><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Site charges:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(SiteCharge) +
    "</span><br />"
);
document.writeln(
  "<span class='lefttext'>Extra charges:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(ExtraCharge) +
    "</span><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Subtotal:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(Subtotal) +
    "</span><br />"
);
document.writeln(
  "<span class='lefttext'>Sales tax (HST):" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(HST) +
    "</span><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Total monthly charges:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(TotMonCharge) +
    "</span><br />"
);
document.writeln(
  "<span class='lefttext'>Monthly dues:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(MonDues) +
    "</span><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Total monthly fees:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(TotMonFee) +
    "</span><br />"
);
document.writeln(
  "<span class='lefttext'>Total yearly fees:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(TotYearFee) +
    "</span><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Monthly payment:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(MonPay) +
    "</span><br /><br /></td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td class='row'>" +
    "<span class='lefttext'>Issued:" +
    "</span>" +
    "<span class='righttext'>" +
    Date +
    "</span><br /><br />"
);
document.writeln(
  "<span class='lefttext'>HST Reg No:" +
    "</span>" +
    "<span class='righttext'>" +
    "549-33-5849" +
    "</span><br /><br />"
);
document.writeln(
  "<span class='lefttext'>Cancellation fee:" +
    "</span>" +
    "<span class='righttext'>" +
    cur2Format.format(CanFee) +
    "</span><br /></td>"
);
document.writeln("</tr>");

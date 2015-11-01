using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace FrontEnd
{
    public partial class VisualizeOnMap : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            ServiceReference1.Service1Client myClient = new ServiceReference1.Service1Client();

            string actualLocation = Label1.Text;
            string calculatedLocation = Label2.Text;
            string result = myClient.findDistance(actualLocation, calculatedLocation);

            string[] processingResult = result.Split(',');

            Label3.Text = result;
            Label4.Text = processingResult[1];
        }

        protected void Button2_Click(object sender, EventArgs e)
        {

        }
    }
}
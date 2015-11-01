using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using System.Xml;
using System.Xml.XPath;
using System.IO;
using System.Net;

namespace PrecisionCalculator
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {

        static string distance;
        static string travelTime;

        public string findDistance(string actualLocation, string computedLocation)
        {

            string myApiQuery = "https://maps.googleapis.com/maps/api/distancematrix/xml?origins="+actualLocation+"&destinations="+computedLocation+"&mode=car&language=en&key=AIzaSyDLQ7xA-rRr2xTxQv2JjxETBeC7KwTaq78";

            XmlDocument queryResult = getXml(myApiQuery);
            string traversedStringFromXml = traverseXml(queryResult);

            return traversedStringFromXml; 
        }

        public XmlDocument getXml(string query)
        {
            HttpWebRequest myWebRequest = WebRequest.Create(query) as HttpWebRequest;
            HttpWebResponse myResponse = myWebRequest.GetResponse() as HttpWebResponse;

            XmlDocument getDoc = new XmlDocument();
            getDoc.Load(myResponse.GetResponseStream());
            return getDoc;
        }

        public static string traverseXml(XmlDocument myDoc)
        {
            XmlNodeList netDistance = myDoc.SelectNodes("DistanceMatrixResponse/element/duration");
            XmlNodeList netTime = myDoc.SelectNodes("DistanceMatrixResponse/element/distance");

           
                foreach (XmlNode myDistance in netDistance)
                {
                    distance = myDistance.SelectSingleNode("text").InnerText + "";
                    break;
                }

                foreach (XmlNode travelDuration in netTime)
                {
                    travelTime = travelDuration.SelectSingleNode("text").InnerText + "";
                    break;
                }

            string result = "Distance between the points is =" + distance + ", travelling time by car is = " + travelTime;

            return result;
        }
    }
}

using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(PrecisionCalculatorFrontEnd.Startup))]
namespace PrecisionCalculatorFrontEnd
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}

"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mn_iot.mac80211.topo import Topo_WiFi

class MyTopo( Topo_WiFi ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo_WiFi.__init__( self )

        # Add hosts and switches
        leftStation = self.addStation( 'sta1' )
        rightStation = self.addStation( 'sta2' )
        leftAP = self.addAccessPoint( 'ap3' )
        rightAP = self.addAccessPoint( 'ap4' )

        # Add links
        self.addLink( leftStation, leftAP )
        self.addLink( leftAP, rightAP )
        self.addLink( rightAP, rightStation )


topos = { 'mytopo': ( lambda: MyTopo() ) }

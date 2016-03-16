def shiftcastorlayout(i, p, *rows):
    i["00 Shift/Castor/" + p] = DQMItem(layout=rows)

# BVB 20160316: Removed Castor from the shift layouts (there are no instructions
#               and as far as we know Castor will not be in before the HI run at
#               the end of the year). We leave the expert workspace for what it
#               is.

##shiftcastorlayout(dqmitems, "01 - Map of frontend and readout errors",
##           [{ 'path': "Castor/CastorDigiMonitor/QIE_capID+er+dv",
##             'description':"Frontend and readout errors"}]
##           )
##
##shiftcastorlayout(dqmitems, "02 - Channel-wise timing",
##           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(Tile TS) (cumulative)",
##             'description':"Channel-wise timing"}]
##           )
##
##shiftcastorlayout(dqmitems, "03 - Map of rechit occupancies",
##           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitOccMap",
##             'description':"Map of rechit occupancies"}]
##           )

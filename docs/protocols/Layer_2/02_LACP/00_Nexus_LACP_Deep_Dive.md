# Nexus LACP Deep Dive


## LACP Basic

1. LACP - Link Aggregation Control Protocol
2. LACP is from 802.1x (formerly 802.3ad)
3. LACP Terms
    * LAG - Link Aggregation Group
        * Connected Port-Channel Interfaces
    * Hot-Standby Link
        * rx/tx packets: no data packets
        * LACP allows max of 16 ports in a port-channel group, but only 8 can be active at a given time. NON-ACTIVE links in an LACP bundle are placed in HOT-STANDBY. Any active turns inactive, one hot standby will move to active. 
        * Conditions:
            * Link Limited by max-bundle 
        * vPC Condition:
            * vPC ports become HOT-STANDBY if **insync_wait_timer** time-out
    * Individual Link
        * rx/tx packets: any packets as normal link 
        * Conditions: not receiving any LACPDU
    * Suspend
        * rx/tx packets: no data packets
        * Conditions:
            * Not receive LACPDU
            * Link failed at LACP nego

    ![LACP Port Status](lacp_port_status.png)





## LACPDU

Link Aggregation Control Protocol Data Unit

* Through LACPDU, interface enabled LACP will transmit several factor to partner
    * System Priority
    * System MAC  -> PO interface MAC, not physical interface MAC. 
    * Interface Priority
    * Interface Number
    * Key

    ![LACPDU_Packet_format](LACPDU_Packet_format.png)




## LAG ID

* **[System Priority + System MAC + Key]** must be same over same LAG in one physical device. 
* System Identifier = **[System Priority + System MAC]**
* Smaller *System Identifier* is in front. 

    ![LAG_ID](LAG_ID.png)

## LACP Status

* Status Code
    
    | Name |1 |0 | 
    |---|---|---| 
    | Activity | Active | Passive|
    | Timeout | Short Timeout | Long Timeout |
    | Aggregatable | Aggregatable | Individual | 
    | Sync | In Sync | Out of Sync |
    | Collecting | Collecting Enabled | Collecting Disabled |
    | Distributing | Enabled | Disabled |
    | Defaulted | Use Default for Partner | Use rx LACPDU for Partner Info |
    | Expired | Partner PDU Expired | Not Expired |  

* LACP Status size in packet: 1 bytes




## LACP Time Summary

### Timer Type

### How to Check LACP Timer

## LACP Status Transition

### LACP Status Transition N7K

### LACP Status Transition N5K

### How to track LACP Status Transition

### Transition Example

## LACP graceful-convergence

## LACP suspend-individual

## LACP and vPC


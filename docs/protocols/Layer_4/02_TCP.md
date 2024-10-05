# TCP basic Breakdown

## TCP Header

### TCP Service

* Transmission-Control-Protocol
* Realiable, ordered, error-checked (adds reliability, but lengthens latency)
* Stream of octets(each byte) service
* Connection oriented  
* Not support Multicast or Broadcast 
* TCP do not care content of byte stream, nor explain to any layer. 
* Intermediate Level between IP and Application Layer (through Network Socket Interface connected to App layer)
* TCP is Full-duplex. 

### TCP Stream

* TCP accepts data from a Data Stream.
    * End Host Processes transmit data by calling TCP;
    * The data will come from Application Layer to Buffer;
    * Then TCP packages the data from buffers into segment; 
    * Then TCP calls IP and transmit. 
* It devides the Data into `chunks`, 
* It adds TCP Header to each chunk and form TCP Segment,
* The Segment is then encapsulated into IP datagram and exchange with peer. 


### Header

TCP Segment consists of 10 mandatory fields and 1 optional extension filed  
    ![TCP_Header](assets/2024-10-01-12-25-36.png)

PCAP of TCP Header:
    ![Wireshark_TCP_Header](assets/2024-10-01-22-23-06.png)

#### Source Port - 16 bits
#### Destination Port - 16 bits

* To confirm a connection requires `src.ip, src.port, dst.ip, dst.port`
* `src.ip + src.port` forms a socket in one host
* Five Tuple : `src.ip src.port dst.ip dst.port protocol `

#### Sequence Number - 32 bits

* Dual Role
    * if SYN flag is set 1, then this is initial sequence number; 
    * If SYN flag is set 0, then this is the accumulated seq number of the first data byte of this segment from current tcp session. 
    * SYN/FIN flag will cost one sequence.

#### Acknoledgment Number - 32 bits

* ACK = sender's seq + 1
* When ACK is set, the value of this field is next sequence number that the responder is expecting.  
* This ACK acknowledge received of all prior bytes. 
* ACK Flag will not cost any sequence. 

#### Data Offset - 4 bits

* Specify size of TCP Header.
* The purpose of the Data Offset is to tell upper layer where the header ends and where the Data starts. 
* Generally when the header is 20 bytes, the Offset will be 0101=5 -> 20 bytes, when there is option in header, like SYN, the Offset may become 1000=8 -> 32 bytes.
* Max of offset is 1111=15 -> 60 bytes


#### Reserved - 3 bits

* Bits of this field are set to 0;
* Reserved for later use
* Sender should not set these bits
* Receiveds should ignore these if set
* Contains in Flags 
    ![Reserved_bit](assets/2024-10-01-22-33-57.png)

* Accurate ECN
    * ECN - Explicit Congestion Notification
    * ECN is a mechanism to let network nodes mark IP packets to indicate congestion to endpoints, rather then drop them. 
    * [RFC7560][1] will reveal more 

#### Flags - 8 bits

* Eight(8) 1-bit-flag as follow:


##### CWR - 1 bit

* Congestion Window Reduced
* CWR to acknowledge that the *Congestion Indicator* echoing was received. 
* CWR is set to indicate:
    * Sender received a TCP segment with ECE flag set
    * and responded in congestion control mechanism 
* [RFC3168][2] will show more detail

##### ECE - ECN-Echo - 1 bit

* ECE is used to echo back the *Congestion indicator* <span style = color:blue>(singal the sender to reduce the transmition rate)</span>.

* Dual Role:
    * If SYN is set as 1, TCP peer is ECN capable
    * If the SYN flag is 0,  ECN=11 will set in its IP header 

    ###### Operations of ECN 

    When ECN is negotiated on a TCP connection:

    * Sender indicate IP header that this is ECN Capable Transport
    * IP header then has the ***Explicit Congestion Notification: ECN-Capable Transport codepoint*** set as `10` 
    
        **TCP Flags**
        ![](assets/2024-10-02-08-57-28.png)

        **IP Flags**
        ![](assets/2024-10-02-08-59-20.png)

    * Intermiate Routes that support ECN will mark those IP Packets with CE`Congestion Experienced 11` code point, instead of dropping them, and send to receiver. 
    * As a result, the flow is marked as singal impending congestion. 
    * When Receiver receives and IP packet with CE code point, the upper layer, TCP, echoes back Congestion Indication using ECE flag in TCP header. 
    * When the original Sender receives TCP segment from original Receiver with ECE bit set, it reduces its Congestion Window and transmission rate 
    * Then the Sender will response a tcp segment with a CWR bit set. 
    * A node keeps transmitting EVE bit set, until it receives a CWR bit set. 
    * Filter with TCPDUMP, `(tcp[13] & 0xc0 != 0)`
    * Require both endpoints and underlaying infrastructe all support such mechanism 

##### URG - 1 bit

* Indicates data in TCP segment is urgent, needs to be processed ASAP, without any waiting for rest of data to arrive. 
* URG flag is accompanied by a 16-bit *urgent pointer* field, 
* *urgent pointer* specifies the *offset* from current sequence number to end of urgent data. 
* Receiver will use *urgent pointer* to locate and process urgent data before normal data. 


##### ACK - 1 bit

* All Packets after the initial SYN packet sent by client should have this set. 

##### PSH - 1 bit

* Ask Receiver to push the buffered data to receiving applicatoin. 

##### RST

* Reset the conneciton.

##### SYN

* Synchronize sequence number.
* Only first packet sent by both should have this bit set. 

##### FIN

* Last packet from both end. 

#### Window

* Receiver's window
* Specify the number of window size units that sender is willing to receive. 

#### Checksum - 16 bits

* Used for Error-Checing of TCP Header, Payload and Pseudo-Header of IP. 
* Consist of IP Pseudo-Header:
    * Src.IP
    * Dst.IP
    * Protocol Number
    * Length of TCP headers and Payload (in bytes)


#### Urgent Pointer - 16 bits

* When URG is set 
* 16 bits is an offset from the current Seq number , indicating the last urgent data byte. 

#### Options

* Variable ~ [0-320 bits], in unit of 32 bits;
* [Size-of-Options] = (Data Offset -5 <!--- 20 bytes of normal header ---> ) * 32

* Options have up to THREE fields:
    
    * Option-kind 
        * 1 byte
        * Indicate type of option
        * NOT optional
        * Next two fields' value is determined by this field.
    * Option-length
        * 1 byte
        * Indicate the total length of OPTION， including OPTION-KIND and OPTION-Length
    * Option-data
        * Size Variable
        * Contains data associated to Option. 


    |OPTION-KIND|OPTION-LENGTH|OPTION-DATA|Purpose|Notes|
    |---|---|---|---|---|
    |0|-|-|End of option list||
    |1|1|-|No-Operation|1. Align options fields on 32-bit boundaries<br>2. Only for padding<br>3. No Operation Option<br>4. 1-byte <br>5. does not have OPTION-Length or Option-Data<br>![](assets/2024-10-04-12-49-31.png)|
    |2|4|SS|MSS<br>Maximum Segment Size|ONLY BE SENT when `SYN` is set![](assets/2024-10-05-09-31-35.png)<br>[MSS](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Maximum_segment_size)|
    |3|3|S|Window Scale|ONLY BE SENT when `SYN` is set|
    |4|2|-|Selective Achnowledgement||
    |5|N(10,18,26,or,34)|BBBB,EEEE,....|Selective ACKnowledgement<br>SACK||
    |8|10|TTTT,EEEE|Timestamp and echo of previous timestamp||
    |28|4|-|User Timeout Option||
    |29|N|-|TCP Authentication Option(TCP-AO)||
    |30|N|-|Multipath TCP||


#### Data









## TCP Connection

### Three-Time Handshake

### Four-Way Handshake

### MSS

### TCP Half-Close

### TCP State

### 2MSL

### FIN_WAIT_2

## TCP Interactive Stream

### Interactive Stream

### Nagle Argorithm

## TCP Sliding Window

### Windows Size

### Sliding Window

### How Wireshark read window size 

### TCP Slow Start

### 

## TCP Re-transmission and Timers

### TCP Timeout Retransmission 

### TCP Fast Transmission

### Selected ACK 

### Duplicated SACK 

### Presist Timer

## TCP Keepalive

## TCP Function 



[1]:[https://www.rfc-editor.org/rfc/rfc7560.txt]
[2]:[https://datatracker.ietf.org/doc/html/rfc3168]

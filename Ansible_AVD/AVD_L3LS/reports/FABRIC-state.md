# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |
| ----------- | ------------------ | ------------------ | ------------------- |
| 304 | 276 | 0 | 28 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |
| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |
| leaf1 | 55 | 51 | 0 | 4 | - | Hardware |
| leaf2 | 55 | 51 | 0 | 4 | - | Hardware |
| leaf3 | 55 | 51 | 0 | 4 | - | Hardware |
| leaf4 | 55 | 51 | 0 | 4 | - | Hardware |
| spine1 | 28 | 24 | 0 | 4 | - | Hardware |
| spine2 | 28 | 24 | 0 | 4 | - | Hardware |
| spine3 | 28 | 24 | 0 | 4 | - | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |
| ------------- | ----------- | ------------ | ------------ | ------------- |
| BGP | 52 | 52 | 0 | 0 |
| Connectivity | 84 | 84 | 0 | 0 |
| Hardware | 28 | 0 | 0 | 28 |
| Interfaces | 79 | 79 | 0 | 0 |
| MLAG | 4 | 4 | 0 | 0 |
| Routing | 43 | 43 | 0 | 0 |
| System | 14 | 14 | 0 | 0 |

## Failed Test Results Summary

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |

## All Test Results

| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |
| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |
| 1 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 2 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 3 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 4 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 10.255.251.1) | PASS | - |
| 5 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.0) | PASS | - |
| 6 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.2) | PASS | - |
| 7 | leaf1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.4) | PASS | - |
| 8 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf2 Ethernet1 | PASS | - |
| 9 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf2 Ethernet2 | PASS | - |
| 10 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet3 | PASS | - |
| 11 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet3 | PASS | - |
| 12 | leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet3 | PASS | - |
| 13 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 14 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 15 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 16 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 17 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 18 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 19 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.1) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 20 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.1) - Destination: spine1 Ethernet3 (IP: 192.168.103.0) | PASS | - |
| 21 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.3) - Destination: spine2 Ethernet3 (IP: 192.168.103.2) | PASS | - |
| 22 | leaf1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.5) - Destination: spine3 Ethernet3 (IP: 192.168.103.4) | PASS | - |
| 23 | leaf1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 24 | leaf1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 25 | leaf1 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 26 | leaf1 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 27 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf2_Ethernet1 = 'up' | PASS | - |
| 28 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf2_Ethernet2 = 'up' | PASS | - |
| 29 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet3 = 'up' | PASS | - |
| 30 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet3 = 'up' | PASS | - |
| 31 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet3 = 'up' | PASS | - |
| 32 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host1_Ethernet1 = 'up' | PASS | - |
| 33 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 34 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 35 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf2_Port-Channel1 = 'up' | PASS | - |
| 36 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host1 = 'up' | PASS | - |
| 37 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 38 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 39 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 40 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 41 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 42 | leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 43 | leaf1 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 44 | leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 45 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 46 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 47 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 48 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 49 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 50 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 51 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 52 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 53 | leaf1 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 54 | leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 55 | leaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 56 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 57 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 58 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 59 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 10.255.251.0) | PASS | - |
| 60 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.6) | PASS | - |
| 61 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.8) | PASS | - |
| 62 | leaf2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.10) | PASS | - |
| 63 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf1 Ethernet1 | PASS | - |
| 64 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf1 Ethernet2 | PASS | - |
| 65 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet4 | PASS | - |
| 66 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet4 | PASS | - |
| 67 | leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet4 | PASS | - |
| 68 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 69 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 70 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 71 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 72 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 73 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 74 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.2) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 75 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.7) - Destination: spine1 Ethernet4 (IP: 192.168.103.6) | PASS | - |
| 76 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.9) - Destination: spine2 Ethernet4 (IP: 192.168.103.8) | PASS | - |
| 77 | leaf2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.11) - Destination: spine3 Ethernet4 (IP: 192.168.103.10) | PASS | - |
| 78 | leaf2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 79 | leaf2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 80 | leaf2 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 81 | leaf2 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 82 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf1_Ethernet1 = 'up' | PASS | - |
| 83 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf1_Ethernet2 = 'up' | PASS | - |
| 84 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet4 = 'up' | PASS | - |
| 85 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet4 = 'up' | PASS | - |
| 86 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet4 = 'up' | PASS | - |
| 87 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host1_Ethernet2 = 'up' | PASS | - |
| 88 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 89 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 90 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf1_Port-Channel1 = 'up' | PASS | - |
| 91 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host1 = 'up' | PASS | - |
| 92 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 93 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 94 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 95 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 96 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 97 | leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 98 | leaf2 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 99 | leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 100 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 101 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 102 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 103 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 104 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 105 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 106 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 107 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 108 | leaf2 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 109 | leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 110 | leaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 111 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 112 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 113 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 114 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 10.255.251.5) | PASS | - |
| 115 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.12) | PASS | - |
| 116 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.14) | PASS | - |
| 117 | leaf3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.16) | PASS | - |
| 118 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf4 Ethernet1 | PASS | - |
| 119 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf4 Ethernet2 | PASS | - |
| 120 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet5 | PASS | - |
| 121 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet5 | PASS | - |
| 122 | leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet5 | PASS | - |
| 123 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 124 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 125 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 126 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 127 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 128 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 129 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.3) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 130 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.13) - Destination: spine1 Ethernet5 (IP: 192.168.103.12) | PASS | - |
| 131 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.15) - Destination: spine2 Ethernet5 (IP: 192.168.103.14) | PASS | - |
| 132 | leaf3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.17) - Destination: spine3 Ethernet5 (IP: 192.168.103.16) | PASS | - |
| 133 | leaf3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 134 | leaf3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 135 | leaf3 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 136 | leaf3 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 137 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf4_Ethernet1 = 'up' | PASS | - |
| 138 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf4_Ethernet2 = 'up' | PASS | - |
| 139 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet5 = 'up' | PASS | - |
| 140 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet5 = 'up' | PASS | - |
| 141 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet5 = 'up' | PASS | - |
| 142 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host3_Ethernet1 = 'up' | PASS | - |
| 143 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 144 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 145 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf4_Port-Channel1 = 'up' | PASS | - |
| 146 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host3 = 'up' | PASS | - |
| 147 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 148 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 149 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 150 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 151 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 152 | leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 153 | leaf3 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 154 | leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 155 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 156 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 157 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 158 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 159 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 160 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 161 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 162 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 163 | leaf3 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 164 | leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 165 | leaf3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 166 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine1 (IP: 192.168.101.11) | PASS | - |
| 167 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine2 (IP: 192.168.101.12) | PASS | - |
| 168 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: spine3 (IP: 192.168.101.13) | PASS | - |
| 169 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 10.255.251.4) | PASS | - |
| 170 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine1 (IP: 192.168.103.18) | PASS | - |
| 171 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine2 (IP: 192.168.103.20) | PASS | - |
| 172 | leaf4 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: spine3 (IP: 192.168.103.22) | PASS | - |
| 173 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet1 - Remote: leaf3 Ethernet1 | PASS | - |
| 174 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet2 - Remote: leaf3 Ethernet2 | PASS | - |
| 175 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: spine1 Ethernet6 | PASS | - |
| 176 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: spine2 Ethernet6 | PASS | - |
| 177 | leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: spine3 Ethernet6 | PASS | - |
| 178 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf1 Loopback0 (IP: 192.168.101.1) | PASS | - |
| 179 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf2 Loopback0 (IP: 192.168.101.2) | PASS | - |
| 180 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf3 Loopback0 (IP: 192.168.101.3) | PASS | - |
| 181 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: leaf4 Loopback0 (IP: 192.168.101.4) | PASS | - |
| 182 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine1 Loopback0 (IP: 192.168.101.11) | PASS | - |
| 183 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine2 Loopback0 (IP: 192.168.101.12) | PASS | - |
| 184 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: Loopback0 (IP: 192.168.101.4) - Destination: spine3 Loopback0 (IP: 192.168.101.13) | PASS | - |
| 185 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.19) - Destination: spine1 Ethernet6 (IP: 192.168.103.18) | PASS | - |
| 186 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.21) - Destination: spine2 Ethernet6 (IP: 192.168.103.20) | PASS | - |
| 187 | leaf4 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.23) - Destination: spine3 Ethernet6 (IP: 192.168.103.22) | PASS | - |
| 188 | leaf4 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 189 | leaf4 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 190 | leaf4 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 191 | leaf4 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 192 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet1 - MLAG_leaf3_Ethernet1 = 'up' | PASS | - |
| 193 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet2 - MLAG_leaf3_Ethernet2 = 'up' | PASS | - |
| 194 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_spine1_Ethernet6 = 'up' | PASS | - |
| 195 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_spine2_Ethernet6 = 'up' | PASS | - |
| 196 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_spine3_Ethernet6 = 'up' | PASS | - |
| 197 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet7 - SERVER_host3_Ethernet2 = 'up' | PASS | - |
| 198 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 199 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback1 - VXLAN_TUNNEL_SOURCE = 'up' | PASS | - |
| 200 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel1 - MLAG_leaf3_Port-Channel1 = 'up' | PASS | - |
| 201 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Port-Channel7 - PortChannel host3 = 'up' | PASS | - |
| 202 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan10 - DMZ = 'up' | PASS | - |
| 203 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan20 - Internal = 'up' | PASS | - |
| 204 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan3009 - MLAG_L3_VRF_VRF_A = 'up' | PASS | - |
| 205 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4093 - MLAG_L3 = 'up' | PASS | - |
| 206 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vlan4094 - MLAG = 'up' | PASS | - |
| 207 | leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Vxlan1 = 'up' | PASS | - |
| 208 | leaf4 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | - | PASS | - |
| 209 | leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 210 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.1 - Peer: leaf1 | PASS | - |
| 211 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.11 - Peer: spine1 | PASS | - |
| 212 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.12 - Peer: spine2 | PASS | - |
| 213 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.13 - Peer: spine3 | PASS | - |
| 214 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.2 - Peer: leaf2 | PASS | - |
| 215 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.3 - Peer: leaf3 | PASS | - |
| 216 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.101.4 - Peer: leaf4 | PASS | - |
| 217 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.1 - Peer: leaf1 | PASS | - |
| 218 | leaf4 | Routing | VerifyRoutingTableEntry | Verifies that the provided routes are present in the routing table of a specified VRF. | Route: 192.168.102.3 - Peer: leaf3 | PASS | - |
| 219 | leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 220 | leaf4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 221 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 222 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 223 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | PASS | - |
| 224 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | PASS | - |
| 225 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.1) | PASS | - |
| 226 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.7) | PASS | - |
| 227 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.13) | PASS | - |
| 228 | spine1 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.19) | PASS | - |
| 229 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet3 | PASS | - |
| 230 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet3 | PASS | - |
| 231 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet3 | PASS | - |
| 232 | spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet3 | PASS | - |
| 233 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.0) - Destination: leaf1 Ethernet3 (IP: 192.168.103.1) | PASS | - |
| 234 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.6) - Destination: leaf2 Ethernet3 (IP: 192.168.103.7) | PASS | - |
| 235 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.12) - Destination: leaf3 Ethernet3 (IP: 192.168.103.13) | PASS | - |
| 236 | spine1 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.18) - Destination: leaf4 Ethernet3 (IP: 192.168.103.19) | PASS | - |
| 237 | spine1 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 238 | spine1 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 239 | spine1 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 240 | spine1 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 241 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet3 = 'up' | PASS | - |
| 242 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet3 = 'up' | PASS | - |
| 243 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet3 = 'up' | PASS | - |
| 244 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet3 = 'up' | PASS | - |
| 245 | spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 246 | spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 247 | spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 248 | spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 249 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 250 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 251 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | PASS | - |
| 252 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | PASS | - |
| 253 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.3) | PASS | - |
| 254 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.9) | PASS | - |
| 255 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.15) | PASS | - |
| 256 | spine2 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.21) | PASS | - |
| 257 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet4 | PASS | - |
| 258 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet4 | PASS | - |
| 259 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet4 | PASS | - |
| 260 | spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet4 | PASS | - |
| 261 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.2) - Destination: leaf1 Ethernet4 (IP: 192.168.103.3) | PASS | - |
| 262 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.8) - Destination: leaf2 Ethernet4 (IP: 192.168.103.9) | PASS | - |
| 263 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.14) - Destination: leaf3 Ethernet4 (IP: 192.168.103.15) | PASS | - |
| 264 | spine2 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.20) - Destination: leaf4 Ethernet4 (IP: 192.168.103.21) | PASS | - |
| 265 | spine2 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 266 | spine2 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 267 | spine2 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 268 | spine2 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 269 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet4 = 'up' | PASS | - |
| 270 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet4 = 'up' | PASS | - |
| 271 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet4 = 'up' | PASS | - |
| 272 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet4 = 'up' | PASS | - |
| 273 | spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 274 | spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 275 | spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 276 | spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |
| 277 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf1 (IP: 192.168.101.1) | PASS | - |
| 278 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf2 (IP: 192.168.101.2) | PASS | - |
| 279 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf3 (IP: 192.168.101.3) | PASS | - |
| 280 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP EVPN Peer: leaf4 (IP: 192.168.101.4) | PASS | - |
| 281 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf1 (IP: 192.168.103.5) | PASS | - |
| 282 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf2 (IP: 192.168.103.11) | PASS | - |
| 283 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf3 (IP: 192.168.103.17) | PASS | - |
| 284 | spine3 | BGP | VerifyBGPSpecificPeers | Verifies the health of specific BGP peer(s) for given address families. | BGP IPv4 Unicast Peer: leaf4 (IP: 192.168.103.23) | PASS | - |
| 285 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet3 - Remote: leaf1 Ethernet5 | PASS | - |
| 286 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet4 - Remote: leaf2 Ethernet5 | PASS | - |
| 287 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet5 - Remote: leaf3 Ethernet5 | PASS | - |
| 288 | spine3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | Local: Ethernet6 - Remote: leaf4 Ethernet5 | PASS | - |
| 289 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet3 (IP: 192.168.103.4) - Destination: leaf1 Ethernet5 (IP: 192.168.103.5) | PASS | - |
| 290 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet4 (IP: 192.168.103.10) - Destination: leaf2 Ethernet5 (IP: 192.168.103.11) | PASS | - |
| 291 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet5 (IP: 192.168.103.16) - Destination: leaf3 Ethernet5 (IP: 192.168.103.17) | PASS | - |
| 292 | spine3 | Connectivity | VerifyReachability | Test network reachability to one or many destination IP(s). | Source: P2P Interface Ethernet6 (IP: 192.168.103.22) - Destination: leaf4 Ethernet5 (IP: 192.168.103.23) | PASS | - |
| 293 | spine3 | Hardware | VerifyEnvironmentCooling | Verifies the status of power supply fans and all fan trays. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentCooling test is not supported on cEOSLab |
| 294 | spine3 | Hardware | VerifyEnvironmentPower | Verifies the power supplies state and input voltage. | Accepted States: 'ok' | SKIPPED | VerifyEnvironmentPower test is not supported on cEOSLab |
| 295 | spine3 | Hardware | VerifyTemperature | Verifies if the device temperature is within acceptable limits. | - | SKIPPED | VerifyTemperature test is not supported on cEOSLab |
| 296 | spine3 | Hardware | VerifyTransceiversManufacturers | Verifies if all the transceivers come from approved manufacturers. | Accepted Manufacturers: 'Arista Networks', 'Arastra, Inc.', 'Not Present' | SKIPPED | VerifyTransceiversManufacturers test is not supported on cEOSLab |
| 297 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet3 - P2P_leaf1_Ethernet5 = 'up' | PASS | - |
| 298 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet4 - P2P_leaf2_Ethernet5 = 'up' | PASS | - |
| 299 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet5 - P2P_leaf3_Ethernet5 = 'up' | PASS | - |
| 300 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Ethernet6 - P2P_leaf4_Ethernet5 = 'up' | PASS | - |
| 301 | spine3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | Interface Loopback0 - ROUTER_ID = 'up' | PASS | - |
| 302 | spine3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | Routing protocol model: multi-agent | PASS | - |
| 303 | spine3 | System | VerifyNTP | Verifies if NTP is synchronised. | - | PASS | - |
| 304 | spine3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | - | PASS | - |

# Discovery Mechanism for KERI: KERID

[KERI](https://github.com/decentralized-identity/keri) is an end-to-end identity system for the Internet that places the primary root-of-trust in self-certifying Autonomic Identifiers (AIDs). Running KERI in indirect mode requires users or controllers to know mappings of AIDs to witness IP addresses in order to communicate and verify identities. KERID solves this problem by providing a discovery mechanism that maps AIDs to witness IDs and witness IDs to witness IPs. This is done using a Distributed Hash Table, Kademlia.

## API

```buildoutcfg
1. POST /id/<aid>/<witness_id>             (publish AID -> ID mapping)
2. GET  /id<aid>                           (get witness ID from AID)
3. POST /ip/<witness_id>/<witness_ip>      (publish ID -> IP mapping)
4. GET  /ip/<witness_id>                   (get witness IP from witness IP)
```

## Running

To bootstrap a new Kademlia cluster (rather than joining an existing one), first run:
```
python3 bootstrap.py
```

Then in another terminal, to get the actual API, run:
```
python3 primary.py
```

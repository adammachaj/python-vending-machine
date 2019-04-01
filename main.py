import machine, item, collector

machine1 = machine.Machine(1)
print(machine1.ITEMS[0])

print(machine1.snacks)

#collector1 = collector.Collector(30)


#machine1.snacks[31] = item.Item("Pepsi")

#print(machine1.snacks.get(31))

#machine1.snacks[32] = item.Item("Cola")
#print(machine1.snacks.get(32))

#collector1.add_item(machine.Machine.ITEMS[1])
#print(collector1)

# print(machine1.snacks[31])

#print(machine1)

machine1.snacks[32].add_item(item.Item("Cola"))
#print(type(machine1.snacks[32]))
# print(machine1.snacks.get(32))
print(machine1.snacks[32])

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        timeslots = []
        for i in range(0, len(arrive)):
            timeslots.append((arrive[i], 1))
            timeslots.append((depart[i], 0))

        timeslots.sort()
        current_active_rooms = 0
        max_active_rooms = 0

        for timeslot in timeslots:
            if timeslot[1] == 1:  # arrival
                current_active_rooms += 1
                max_active_rooms = max(max_active_rooms, current_active_rooms)
            else:  # departure
                current_active_rooms -= 1

        return K >= max_active_rooms

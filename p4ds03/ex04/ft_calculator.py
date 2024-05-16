class calculator:
    """A calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Return the scalar dot of the two given vectors"""
        final_result = 0
        for i in range(len(V1)):
            final_result += V1[i] * V2[i]
        print(f"Dot product is: {final_result}")
            

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """return addition of the two given vectors"""
        V3 = [x for x in V1]
        for i in range(len(V1)):
            V3[i] = float(V3[i] + V2[i])
        print(f"Add vector is: {V3}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Return the soustraction of the two given vectors"""
        V3 = [x for x in V1]
        for i in range(len(V1)):
            V3[i] = float(V3[i] - V2[i])
        print(f"Sous vector is: {V3}")
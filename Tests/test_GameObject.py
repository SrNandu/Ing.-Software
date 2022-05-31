from gameObject import gameObject


class test_gameObject:

    def testMoverPositivo():
        obj = gameObject()
        obj.mover(300, 250)
        assert obj.getPosicion == (300, 250)
        
    def testMoverNegativo():
        obj = gameObject()
        obj.mover(-300, -250)
        assert obj.getPosicion == (-300, -250)

    def testMoverCero():
        obj = gameObject()
        obj.mover(0, 0)
        assert obj.getPosicion == (0, 0)
    
    def testMoverAfuera():
        obj = gameObject()
        obj.mover(-1000, 1000)
        assert obj.getPosicion == (-300, -250)

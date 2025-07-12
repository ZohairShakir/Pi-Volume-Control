from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
current_scalar = volume.GetMasterVolumeLevelScalar()
new_scalar = min(current_scalar + 0.01, 1.0)  # +1%
i=0
x=3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342559408
x=str(x)
print(len(str(x)))
e=[]
a=int(input("increase(1) or decrease(0)"))
if a == 1:
    for i in range(0,101):
        d=int(input("write the digits of pi?(excluding .)"))
        print(d)
        if d == int(x[i]):
            print("volume raised by 1%")
            current_scalar = min(current_scalar + 0.01, 1.0)
            volume.SetMasterVolumeLevelScalar(current_scalar, None)
            i=i+1
        else:
            print("fk off")
elif a == 0:
    for i in range(0,101):
        d=int(input("write the digits of pi?(excluding .)"))
        print(d)
        if d == int(x[i]):
            print("volume decreased by 1%")
            current_scalar = min(current_scalar - 0.01, 1.0)
            volume.SetMasterVolumeLevelScalar(current_scalar, None)
            i=i+1
        else:
            print("nooooooooooo")

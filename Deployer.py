import pyautogui
import time

time.sleep(6)

cpp_code = r"""
supra move tool init --package-dir /supra/configs/move_workspace/Seventh --name Seventh
"""
pyautogui.typewrite(cpp_code, interval=0.03)

time.sleep(15)

cpp_code = r"""
docker cp c617a290da2e3394d56a083ef24a885728cf96a5309f83deabec5747007f99db:/supra/configs/move_workspace/Seventh C:\Users\Lenovo\Desktop
"""

pyautogui.typewrite(cpp_code, interval=0.02)

time.sleep(30)

cpp_code = r"""
//:!:>moon
module MoonCoin::moon_coin {
    use aptos_framework::coin;

    struct MoonCoin {}

    fun init_module(sender: &signer) {
        aptos_framework::managed_coin::initialize<MoonCoin>(
            sender,
            b"Moon Coin",
            b"MOON",
            6,
            false,
        );
    }

    public entry fun register(account: &signer) {
        aptos_framework::managed_coin::register<MoonCoin>(account)
    }

    public entry fun mint(account: &signer, dst_addr: address, amount: u64) {
        aptos_framework::managed_coin::mint<MoonCoin>(account, dst_addr, amount);
    }

    public entry fun burn(account: &signer, amount: u64) {
        aptos_framework::managed_coin::burn<MoonCoin>(account, amount);
    }

    public entry fun transfer(from: &signer, to: address, amount: u64,) {
        coin::transfer<MoonCoin>(from, to, amount);
    }
}
//<:!:moon
"""

pyautogui.typewrite(cpp_code, interval=0.01)

time.sleep(20)

cpp_code = r"""
[package]
name = "moon_coin"
version = "1.0.0"
authors = []

[addresses]
MoonCoin = "0xa9aa1587371e78286391d86d7e951cf2c177e5d48eb494387e74eefcc53d6217"
[dev-addresses]

[dependencies]
AptosFramework = { git = "https://github.com/aptos-labs/aptos-core.git", subdir = "aptos-move/framework/aptos-framework/", rev = "eb0144a39ada521d8dee01c9dbd601853d383fb3" }
SupraVrf = { git = "https://github.com/Entropy-Foundation/vrf-interface", subdir = "aptos/testnet", rev = "ff49e3688411d2374f75994a8713f86a5760868a"  }

[dev-dependencies]"""

pyautogui.typewrite(cpp_code, interval=0.01)
time.sleep(15)

cpp_code = r"""
docker cp C:\Users\Lenovo\Desktop\Seventh c617a290da2e3394d56a083ef24a885728cf96a5309f83deabec5747007f99db:/supra/configs/move_workspace/"""

pyautogui.typewrite(cpp_code, interval=0.02)

time.sleep(20)

cpp_code = r"""
supra move tool compile --package-dir /supra/configs/move_workspace/Seventh
"""

pyautogui.typewrite(cpp_code, interval=0.02)

time.sleep(30)

cpp_code = r"""
supra move tool publish --package-dir /supra/configs/move_workspace/Seventh --profile tussu --url https://rpc-testnet.supra.com
"""

pyautogui.typewrite(cpp_code, interval=0.02)

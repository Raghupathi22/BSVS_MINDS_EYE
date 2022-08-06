// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract BSVS {

    string public name;

    constructor (string memory bsvs) {
        name = bsvs;
    }

    function set(string memory seed_name) public {
        name = seed_name;
    }

    function set1(string memory location) public {
        name = location;
    }
    function set2(string memory mandate) public {
        name = mandate;
}
    function set3(string memory expdate) public {
        name = expdate;
}
}
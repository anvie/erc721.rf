pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

contract HasRoot {
    address private _root;

    event RootChanged(address indexed newRoot);

    modifier onlyRoot {
        _onlyRoot();
        _;
    }

    function _onlyRoot() private view {
        require(_isRoot(msg.sender), "Only root may perform this action");
    }

    function root() public view returns(address) {
        return _root;
    }

    function _setRoot(address account) internal {
        _root = account;
        emit RootChanged(_root);
    }

    function _isRoot(address account) internal view returns(bool) {
        return account == _root;
    }

}
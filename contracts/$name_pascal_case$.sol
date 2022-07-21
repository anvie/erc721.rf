pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./HasAdmin.sol";


contract $name_pascal_case$ is
    ERC721,
    Ownable,
    HasAdmin
{
    using Counters for Counters.Counter;

    uint256 public constant maxSupply = $param.max_supply$;

    Counters.Counter private _idGen;

    string public baseTokenURI;

    event ItemMinted(uint256 indexed tokenId);

    constructor(string memory _baseTokenURI, address admin)
        ERC721("$name$", "$param.token_code$")
    {
        baseTokenURI = _baseTokenURI;
        _setAdmin(admin);
        _idGen.reset();
    }

    modifier onlyAdminOrOwner() {
        require(
            _isAdmin(_msgSender()) || owner() == _msgSender(),
            "Only owner or admin can set daily aging rate"
        );
        _;
    }

    function changeAdmin(address newAdmin) external onlyOwner {
        _setAdmin(newAdmin);
    }

    function mint(address to) external returns(uint256) {
        _idGen.increment();
        uint256 tokenId = _idGen.current();

        require(tokenId <= maxSupply, "max supply exceeded");

        _safeMint(to, tokenId);

        emit ItemMinted(tokenId);

        return tokenId;
    }

    function totalSupply() external view returns(uint256) {
        return _idGen.current();
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    function setBaseURI(string memory baseURI) public onlyOwner {
        baseTokenURI = baseURI;
    }
}

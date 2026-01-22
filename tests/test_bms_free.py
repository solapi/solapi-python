import pytest

from solapi.model.kakao.bms import (
    BmsAppButton,
    BmsCarouselCommerceItem,
    BmsCarouselCommerceSchema,
    BmsCarouselFeedItem,
    BmsCarouselFeedSchema,
    BmsCommerce,
    BmsCoupon,
    BmsMainWideItem,
    BmsOption,
    BmsSubWideItem,
    BmsVideo,
    BmsWebButton,
)
from solapi.model.request.kakao.bms import Bms


class TestBmsCommerce:
    def test_valid_regular_price_only(self):
        commerce = BmsCommerce(title="상품명", regular_price=10000)
        assert commerce.title == "상품명"
        assert commerce.regular_price == 10000

    def test_valid_discount_rate(self):
        commerce = BmsCommerce(
            title="상품명",
            regular_price=10000,
            discount_price=8000,
            discount_rate=20,
        )
        assert commerce.discount_rate == 20

    def test_valid_discount_fixed(self):
        commerce = BmsCommerce(
            title="상품명",
            regular_price=10000,
            discount_price=8000,
            discount_fixed=2000,
        )
        assert commerce.discount_fixed == 2000

    def test_invalid_both_discount_types(self):
        with pytest.raises(ValueError, match="discountRate와 discountFixed는 동시에"):
            BmsCommerce(
                title="상품명",
                regular_price=10000,
                discount_price=8000,
                discount_rate=20,
                discount_fixed=2000,
            )

    def test_invalid_discount_rate_without_price(self):
        with pytest.raises(ValueError, match="discountPrice.*함께 지정"):
            BmsCommerce(
                title="상품명",
                regular_price=10000,
                discount_rate=20,
            )

    def test_invalid_discount_price_alone(self):
        with pytest.raises(ValueError, match="discountRate.*discountFixed.*함께"):
            BmsCommerce(
                title="상품명",
                regular_price=10000,
                discount_price=8000,
            )

    def test_string_to_int_coercion(self):
        commerce = BmsCommerce(title="상품명", regular_price="10000")  # type: ignore[arg-type]
        assert commerce.regular_price == 10000


class TestBmsCoupon:
    def test_valid_won_discount(self):
        coupon = BmsCoupon(title="5000원 할인 쿠폰", description="설명")
        assert coupon.title == "5000원 할인 쿠폰"

    def test_valid_percent_discount(self):
        coupon = BmsCoupon(title="10% 할인 쿠폰", description="설명")
        assert coupon.title == "10% 할인 쿠폰"

    def test_valid_shipping_discount(self):
        coupon = BmsCoupon(title="배송비 할인 쿠폰", description="설명")
        assert coupon.title == "배송비 할인 쿠폰"

    def test_valid_free_coupon(self):
        coupon = BmsCoupon(title="커피 무료 쿠폰", description="설명")
        assert coupon.title == "커피 무료 쿠폰"

    def test_valid_up_coupon(self):
        coupon = BmsCoupon(title="포인트 UP 쿠폰", description="설명")
        assert coupon.title == "포인트 UP 쿠폰"

    def test_invalid_coupon_title(self):
        with pytest.raises(ValueError, match="쿠폰 제목은 다음 형식"):
            BmsCoupon(title="잘못된 쿠폰", description="설명")


class TestBmsVideo:
    def test_valid_kakao_tv_url(self):
        video = BmsVideo(video_url="https://tv.kakao.com/v/123456")
        assert video.video_url == "https://tv.kakao.com/v/123456"

    def test_invalid_url(self):
        with pytest.raises(ValueError, match="카카오TV 동영상 링크"):
            BmsVideo(video_url="https://youtube.com/watch?v=123")


class TestBmsButton:
    def test_web_button(self):
        button = BmsWebButton(name="버튼", link_mobile="https://example.com")
        assert button.link_type == "WL"
        assert button.name == "버튼"

    def test_app_button_with_mobile(self):
        button = BmsAppButton(name="앱 버튼", link_mobile="https://example.com")
        assert button.link_type == "AL"

    def test_app_button_with_android(self):
        button = BmsAppButton(name="앱 버튼", link_android="app://path")
        assert button.link_android == "app://path"

    def test_app_button_without_links(self):
        with pytest.raises(
            ValueError, match="linkMobile, linkAndroid, linkIos 중 하나"
        ):
            BmsAppButton(name="앱 버튼")


class TestBmsWideItem:
    def test_main_wide_item(self):
        item = BmsMainWideItem(image_id="img123", link_mobile="https://example.com")
        assert item.image_id == "img123"
        assert item.title is None

    def test_sub_wide_item(self):
        item = BmsSubWideItem(
            title="서브 아이템",
            image_id="img123",
            link_mobile="https://example.com",
        )
        assert item.title == "서브 아이템"


class TestBmsCarousel:
    def test_feed_schema(self):
        items = [
            BmsCarouselFeedItem(
                header="헤더1",
                content="내용1",
                image_id="img1",
                buttons=[BmsWebButton(name="버튼", link_mobile="https://example.com")],
            ),
            BmsCarouselFeedItem(
                header="헤더2",
                content="내용2",
                image_id="img2",
                buttons=[BmsWebButton(name="버튼", link_mobile="https://example.com")],
            ),
        ]
        schema = BmsCarouselFeedSchema(items=items)
        assert schema.items is not None
        assert len(schema.items) == 2

    def test_commerce_schema(self):
        items = [
            BmsCarouselCommerceItem(
                commerce=BmsCommerce(title="상품1", regular_price=10000),
                image_id="img1",
                buttons=[BmsWebButton(name="구매", link_mobile="https://example.com")],
            ),
            BmsCarouselCommerceItem(
                commerce=BmsCommerce(title="상품2", regular_price=20000),
                image_id="img2",
                buttons=[BmsWebButton(name="구매", link_mobile="https://example.com")],
            ),
        ]
        schema = BmsCarouselCommerceSchema(items=items)
        assert schema.items is not None
        assert len(schema.items) == 2


class TestBmsOption:
    def test_text_type_minimal(self):
        bms = BmsOption(targeting="I", chat_bubble_type="TEXT")
        assert bms.targeting == "I"
        assert bms.chat_bubble_type == "TEXT"

    def test_image_type_requires_image_id(self):
        with pytest.raises(ValueError, match="imageId"):
            BmsOption(targeting="I", chat_bubble_type="IMAGE")

    def test_image_type_valid(self):
        bms = BmsOption(targeting="I", chat_bubble_type="IMAGE", image_id="img123")
        assert bms.image_id == "img123"

    def test_wide_type_requires_image_id(self):
        with pytest.raises(ValueError, match="imageId"):
            BmsOption(targeting="I", chat_bubble_type="WIDE")

    def test_wide_item_list_requires_minimum_sub_items(self):
        main_item = BmsMainWideItem(image_id="img", link_mobile="https://example.com")
        sub_items = [
            BmsSubWideItem(
                title="1", image_id="img1", link_mobile="https://example.com"
            ),
            BmsSubWideItem(
                title="2", image_id="img2", link_mobile="https://example.com"
            ),
        ]
        with pytest.raises(ValueError, match="최소 3개"):
            BmsOption(
                targeting="I",
                chat_bubble_type="WIDE_ITEM_LIST",
                header="헤더",
                main_wide_item=main_item,
                sub_wide_item_list=sub_items,
            )

    def test_wide_item_list_valid(self):
        main_item = BmsMainWideItem(image_id="img", link_mobile="https://example.com")
        sub_items = [
            BmsSubWideItem(
                title="1", image_id="img1", link_mobile="https://example.com"
            ),
            BmsSubWideItem(
                title="2", image_id="img2", link_mobile="https://example.com"
            ),
            BmsSubWideItem(
                title="3", image_id="img3", link_mobile="https://example.com"
            ),
        ]
        bms = BmsOption(
            targeting="I",
            chat_bubble_type="WIDE_ITEM_LIST",
            header="헤더",
            main_wide_item=main_item,
            sub_wide_item_list=sub_items,
        )
        assert bms.sub_wide_item_list is not None
        assert len(bms.sub_wide_item_list) == 3

    def test_commerce_requires_fields(self):
        with pytest.raises(ValueError, match="imageId.*commerce.*buttons"):
            BmsOption(targeting="I", chat_bubble_type="COMMERCE")

    def test_commerce_valid(self):
        bms = BmsOption(
            targeting="I",
            chat_bubble_type="COMMERCE",
            image_id="img123",
            commerce=BmsCommerce(title="상품", regular_price=10000),
            buttons=[BmsWebButton(name="구매", link_mobile="https://example.com")],
        )
        assert bms.commerce is not None
        assert bms.commerce.title == "상품"

    def test_carousel_feed_requires_carousel(self):
        with pytest.raises(ValueError, match="carousel"):
            BmsOption(targeting="I", chat_bubble_type="CAROUSEL_FEED")

    def test_premium_video_requires_video(self):
        with pytest.raises(ValueError, match="video"):
            BmsOption(targeting="I", chat_bubble_type="PREMIUM_VIDEO")

    def test_premium_video_valid(self):
        bms = BmsOption(
            targeting="I",
            chat_bubble_type="PREMIUM_VIDEO",
            video=BmsVideo(video_url="https://tv.kakao.com/v/123"),
        )
        assert bms.video is not None
        assert bms.video.video_url == "https://tv.kakao.com/v/123"


class TestBms:
    def test_bms_without_chat_bubble_type(self):
        bms = Bms(targeting="I")
        assert bms.targeting == "I"
        assert bms.chat_bubble_type is None

    def test_bms_with_text_type(self):
        bms = Bms(targeting="I", chat_bubble_type="TEXT")
        assert bms.chat_bubble_type == "TEXT"

    def test_bms_serialization(self):
        bms = Bms(
            targeting="I",
            chat_bubble_type="TEXT",
            additional_content="추가 내용",
        )
        data = bms.model_dump(by_alias=True, exclude_none=True)
        assert data["targeting"] == "I"
        assert data["chatBubbleType"] == "TEXT"
        assert data["additionalContent"] == "추가 내용"


class TestBmsFreeE2E:
    """E2E tests for BMS Free message sending.

    These tests actually send messages through the SOLAPI API.
    Requires SOLAPI_KAKAO_PF_ID environment variable to be set.
    """

    def test_send_bms_text_minimal(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE TEXT type with minimal structure."""
        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        message = RequestMessage(
            from_=test_phone_numbers["sender"],
            to=test_phone_numbers["recipient"],
            text="[테스트] BMS FREE TEXT 최소 구조 테스트입니다.",
            type=MessageType.BMS_FREE,
            kakao_options=KakaoOption(
                pf_id=pf_id,
                bms=Bms(targeting="I", chat_bubble_type="TEXT"),
            ),
        )

        try:
            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE TEXT test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_text_with_buttons(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE TEXT type with buttons and coupon."""
        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        message = RequestMessage(
            from_=test_phone_numbers["sender"],
            to=test_phone_numbers["recipient"],
            text="[테스트] BMS FREE TEXT 전체 필드 테스트입니다.",
            type=MessageType.BMS_FREE,
            kakao_options=KakaoOption(
                pf_id=pf_id,
                bms=Bms(
                    targeting="I",
                    chat_bubble_type="TEXT",
                    adult=False,
                    buttons=[
                        BmsWebButton(name="웹 링크", link_mobile="https://example.com"),
                        BmsAppButton(
                            name="앱 링크",
                            link_mobile="https://example.com",
                            link_android="exampleapp://path",
                            link_ios="exampleapp://path",
                        ),
                    ],
                    coupon=BmsCoupon(
                        title="10% 할인 쿠폰",
                        description="테스트 쿠폰입니다.",
                        link_mobile="https://example.com/coupon",
                    ),
                ),
            ),
        )

        try:
            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE TEXT with buttons test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_image(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE IMAGE type with image upload."""
        from pathlib import Path

        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.request.storage import FileTypeEnum
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        try:
            file_response = message_service.upload_file(
                file_path=str(image_path),
                upload_type=FileTypeEnum.BMS,
            )
            image_id = file_response.file_id
            print(f"Uploaded BMS image ID: {image_id}")

            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                text="[테스트] BMS FREE IMAGE 테스트입니다.",
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="IMAGE",
                        image_id=image_id,
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE IMAGE test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_commerce(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE COMMERCE type with product info."""
        from pathlib import Path

        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.request.storage import FileTypeEnum
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        try:
            file_response = message_service.upload_file(
                file_path=str(image_path),
                upload_type=FileTypeEnum.BMS,
            )
            image_id = file_response.file_id

            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="COMMERCE",
                        image_id=image_id,
                        commerce=BmsCommerce(
                            title="테스트 상품",
                            regular_price=50000,
                            discount_price=40000,
                            discount_rate=20,
                        ),
                        buttons=[
                            BmsWebButton(
                                name="구매하기",
                                link_mobile="https://example.com/product",
                            ),
                        ],
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE COMMERCE test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_wide(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE WIDE type."""
        from pathlib import Path

        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.request.storage import FileTypeEnum
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        try:
            file_response = message_service.upload_file(
                file_path=str(image_path),
                upload_type=FileTypeEnum.BMS_WIDE,
            )
            image_id = file_response.file_id
            print(f"Uploaded BMS WIDE image ID: {image_id}")

            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                text="[테스트] BMS FREE WIDE 테스트입니다.",
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="WIDE",
                        image_id=image_id,
                        buttons=[
                            BmsWebButton(
                                name="자세히 보기",
                                link_mobile="https://example.com",
                            ),
                        ],
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE WIDE test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_wide_item_list(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE WIDE_ITEM_LIST type.

        Note: Main item requires 2:1 ratio, sub items require 1:1 ratio.
        """
        from pathlib import Path

        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.request.storage import FileTypeEnum
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        main_image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example_wide.jpg"
        )
        sub_image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example_square.jpg"
        )
        if not main_image_path.exists():
            pytest.skip(f"2:1 ratio test image not found at {main_image_path}")
        if not sub_image_path.exists():
            pytest.skip(f"1:1 ratio test image not found at {sub_image_path}")

        try:
            main_file_response = message_service.upload_file(
                file_path=str(main_image_path),
                upload_type=FileTypeEnum.BMS_WIDE_MAIN_ITEM_LIST,
            )
            main_image_id = main_file_response.file_id
            print(f"Uploaded main image ID: {main_image_id}")

            sub_file_response = message_service.upload_file(
                file_path=str(sub_image_path),
                upload_type=FileTypeEnum.BMS_WIDE_SUB_ITEM_LIST,
            )
            sub_image_id = sub_file_response.file_id
            print(f"Uploaded sub image ID: {sub_image_id}")

            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="WIDE_ITEM_LIST",
                        header="와이드 아이템 리스트 테스트",
                        main_wide_item=BmsMainWideItem(
                            image_id=main_image_id,
                            title="메인 아이템",
                            link_mobile="https://example.com/main",
                        ),
                        sub_wide_item_list=[
                            BmsSubWideItem(
                                image_id=sub_image_id,
                                title="서브 아이템 1",
                                link_mobile="https://example.com/sub1",
                            ),
                            BmsSubWideItem(
                                image_id=sub_image_id,
                                title="서브 아이템 2",
                                link_mobile="https://example.com/sub2",
                            ),
                            BmsSubWideItem(
                                image_id=sub_image_id,
                                title="서브 아이템 3",
                                link_mobile="https://example.com/sub3",
                            ),
                        ],
                        buttons=[
                            BmsWebButton(
                                name="더보기",
                                link_mobile="https://example.com",
                            ),
                        ],
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE WIDE_ITEM_LIST test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_carousel_feed(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE CAROUSEL_FEED type."""
        from pathlib import Path

        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.request.storage import FileTypeEnum
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        try:
            file_response = message_service.upload_file(
                file_path=str(image_path),
                upload_type=FileTypeEnum.BMS_CAROUSEL_FEED_LIST,
            )
            image_id = file_response.file_id
            print(f"Uploaded carousel feed image ID: {image_id}")

            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="CAROUSEL_FEED",
                        carousel=BmsCarouselFeedSchema(
                            items=[
                                BmsCarouselFeedItem(
                                    header="첫 번째 카드",
                                    content="캐러셀 피드 테스트 메시지입니다.",
                                    image_id=image_id,
                                    buttons=[
                                        BmsWebButton(
                                            name="자세히 보기",
                                            link_mobile="https://example.com/1",
                                        ),
                                    ],
                                ),
                                BmsCarouselFeedItem(
                                    header="두 번째 카드",
                                    content="두 번째 캐러셀 아이템입니다.",
                                    image_id=image_id,
                                    buttons=[
                                        BmsWebButton(
                                            name="자세히 보기",
                                            link_mobile="https://example.com/2",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE CAROUSEL_FEED test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_carousel_commerce(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE CAROUSEL_COMMERCE type."""
        from pathlib import Path

        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.request.storage import FileTypeEnum
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        image_path = (
            Path(__file__).parent.parent / "examples" / "images" / "example.jpg"
        )
        if not image_path.exists():
            pytest.skip(f"Test image not found at {image_path}")

        try:
            file_response = message_service.upload_file(
                file_path=str(image_path),
                upload_type=FileTypeEnum.BMS_CAROUSEL_COMMERCE_LIST,
            )
            image_id = file_response.file_id
            print(f"Uploaded carousel commerce image ID: {image_id}")

            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="CAROUSEL_COMMERCE",
                        carousel=BmsCarouselCommerceSchema(
                            items=[
                                BmsCarouselCommerceItem(
                                    image_id=image_id,
                                    commerce=BmsCommerce(
                                        title="상품 1",
                                        regular_price=50000,
                                        discount_price=40000,
                                        discount_rate=20,
                                    ),
                                    buttons=[
                                        BmsWebButton(
                                            name="구매하기",
                                            link_mobile="https://example.com/product1",
                                        ),
                                    ],
                                ),
                                BmsCarouselCommerceItem(
                                    image_id=image_id,
                                    commerce=BmsCommerce(
                                        title="상품 2",
                                        regular_price=80000,
                                        discount_price=60000,
                                        discount_fixed=20000,
                                    ),
                                    buttons=[
                                        BmsWebButton(
                                            name="구매하기",
                                            link_mobile="https://example.com/product2",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE CAROUSEL_COMMERCE test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

    def test_send_bms_premium_video(
        self, message_service, test_phone_numbers, test_kakao_options
    ):
        """Test sending BMS FREE PREMIUM_VIDEO type."""
        from solapi.model import RequestMessage
        from solapi.model.kakao.kakao_option import KakaoOption
        from solapi.model.message_type import MessageType
        from solapi.model.request.kakao.bms import Bms
        from solapi.model.response.send_message_response import SendMessageResponse

        pf_id = test_kakao_options.get("pf_id", "")
        if not pf_id or pf_id == "계정에 등록된 카카오 비즈니스 채널ID":
            pytest.skip("SOLAPI_KAKAO_PF_ID not configured")

        try:
            message = RequestMessage(
                from_=test_phone_numbers["sender"],
                to=test_phone_numbers["recipient"],
                text="[테스트] BMS FREE PREMIUM_VIDEO 테스트입니다.",
                type=MessageType.BMS_FREE,
                kakao_options=KakaoOption(
                    pf_id=pf_id,
                    bms=Bms(
                        targeting="I",
                        chat_bubble_type="PREMIUM_VIDEO",
                        video=BmsVideo(
                            video_url="https://tv.kakao.com/v/123456789",
                        ),
                        buttons=[
                            BmsWebButton(
                                name="영상 보기",
                                link_mobile="https://tv.kakao.com/v/123456789",
                            ),
                        ],
                    ),
                ),
            )

            response = message_service.send(message)
        except Exception as e:
            pytest.skip(f"BMS FREE PREMIUM_VIDEO test skipped: {e}")

        assert isinstance(response, SendMessageResponse)
        assert response.group_info is not None
        assert response.group_info.count.total > 0

        print(f"Group ID: {response.group_info.group_id}")
        print(f"Total: {response.group_info.count.total}")
        print(f"Success: {response.group_info.count.registered_success}")

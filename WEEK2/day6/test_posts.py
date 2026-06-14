import pytest

class TestPosts:
    #1.获取所有文章
    def test_get_all_posts(self,api_session,base_url):
        response  = api_session.get(f"{base_url}/posts")
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts,list)
        assert len(posts) == 100

    #2.参数化获取单篇文章
    @pytest.mark.parametrize("post_id",[1,2,3,10,50])
    def test_get_single_post(self,api_session,base_url,post_id):
        response = api_session.get(f"{base_url}/posts/{post_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == post_id
    
    #3.数据结构完整性
    def test_post_str(self,api_session,base_url):
        response = api_session.get(f"{base_url}/posts/1")
        assert response.status_code == 200
        from conftest import assert_post_structure
        assert_post_structure(response.json())

    #4.按用户 ID 筛选文章
    @pytest.mark.parametrize("user_id",[1,2,3,10])
    def test_filter_posts_by_user(self,api_session,base_url,user_id):
        response = api_session.get(f"{base_url}/posts",params={"userId":user_id})
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == 10

    #5.创建文章
    def test_cre_post(self,api_session,base_url,sample_post):
        response = api_session.post(f"{base_url}/posts",json=sample_post)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_post["title"]
        assert data["id"] == 101

    #6.创建文章并验证关键字段返回
    def test_cre_post_returns_cor_fields(self,api_session,base_url,sample_post):
        response = api_session.post(f"{base_url}/posts",json=sample_post)
        assert response.status_code == 201
        data = response.json()
        for key in sample_post:
            assert data[key] == sample_post[key]
    
    #7.边界值：空标题创建
    def test_cre_post_with_empty_title(self,api_session,base_url):
        payload = {"title":"","body":"无标题","userId":1}
        response = api_session.post(f"{base_url}/posts",json=payload)
        assert response.status_code == 201

    #8.边界值：超长标题创建
    def test_cre_post_with_long_title(self,api_session,base_url):
        payload = {"title":"A"*500,"body":"B"*500,"userId":1}
        response = api_session.post(f"{base_url}/posts",json=payload)
        assert response.status_code == 201

    #9.更新文章 PUT
    def test_update_post(self,api_session,base_url,sample_post):
        sample_post["title"] = "更新后的标题"
        response = api_session.put(f"{base_url}/posts/1",json=sample_post)
        assert response.status_code == 200
        assert response.json()["title"] == "更新后的标题"

    #10.部分更新 PATCH
    def test_patch_post(self,api_session,base_url):
        response = api_session.patch(
            f"{base_url}/posts/1",
            json={"title":"仅更新标题"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "仅更新标题"
        assert "body" in data

    #11.删除文章
    def test_del_post(delf,api_session,base_url):
        response = api_session.delete(f"{base_url}/posts/1")
        assert response.status_code == 200
        assert response.json() == {}

    #12.获取不存在的文章
    def test_get_none_post(self,api_session,base_url):
        response = api_session.get(f"{base_url}/posts/99999")
        assert response.status_code == 404

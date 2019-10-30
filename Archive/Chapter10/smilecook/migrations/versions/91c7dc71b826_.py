"""empty message

Revision ID: 91c7dc71b826
Revises: 7aafe51af016
Create Date: 2019-09-22 12:06:36.061632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91c7dc71b826'
down_revision = '7aafe51af016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('cover_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'cover_image')
    # ### end Alembic commands ###